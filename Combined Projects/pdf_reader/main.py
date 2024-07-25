import os

# Set environment variable to allow multiple OpenMP runtimes
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

from flask import Flask, request, jsonify, send_from_directory, render_template
import pytesseract
from pdf2image import convert_from_path
import tempfile
import torch
import faiss
import numpy as np
from transformers import pipeline
from langdetect import detect, LangDetectException
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
import difflib
import shutil

# Ensure NLTK data is downloaded
nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)

# Load pre-trained models for QA, summarization, and text similarity
qa_model = pipeline('question-answering', model="DeepPavlov/bert-base-cased-conversational")
summarizer = pipeline("summarization", model="cointegrated/rut5-base-multitask")
nlp = pipeline('feature-extraction', model="sberbank-ai/ruBert-base", tokenizer="sberbank-ai/ruBert-base")

stop_words = set(nltk.corpus.stopwords.words('russian'))

def extract_text_from_images_page(pdf_path, page_number):
    try:
        pages = convert_from_path(pdf_path, 300, first_page=page_number + 1, last_page=page_number + 1)
        if pages:
            text = pytesseract.image_to_string(pages[0], lang='rus+eng')
            print(f"Extracted text from image of page {page_number}: {text[:200]}...")
            return text
        return None
    except Exception as e:
        print(f"Failed to convert page {page_number} to image: {e}")
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<path:path>')
def static_file(path):
    return send_from_directory('static', path)

@app.route('/analyze', methods=['POST'])
def analyze_pdf():
    print("Received files:", request.files)
    print("Received form data:", request.form)

    pdf_file = request.files.get('file')
    query = request.form.get('query')

    if not pdf_file or not query:
        return jsonify({'error': 'No file or search query provided'}), 400

    # Save PDF to a temporary file
    temp_dir = tempfile.mkdtemp()
    temp_pdf_path = os.path.join(temp_dir, pdf_file.filename)
    pdf_file.save(temp_pdf_path)

    combined_text = ""
    page_number = 0

    while True:
        # Try to extract text from the current page
        text = extract_text_from_images_page(temp_pdf_path, page_number)
        if not text:
            break  # Exit loop if no text is found

        print(f"Full text from page {page_number}: {text}")

        # Combine all text
        combined_text += " " + text
        page_number += 1

    # Clean up temporary files
    os.remove(temp_pdf_path)
    shutil.rmtree(temp_dir)

    if not combined_text.strip():
        return jsonify({"summary": "No relevant information found in the document."})

    # Prepare FAISS index
    sentences = sent_tokenize(combined_text)
    russian_sentences = []
    for sentence in sentences:
        if len(sentence.strip()) > 10:  # Only consider sentences with more than 10 characters
            try:
                if detect(sentence) == 'ru':
                    russian_sentences.append(sentence)
            except LangDetectException:
                continue

    if not russian_sentences:
        return jsonify({"summary": "No Russian sentences extracted from the combined text."})

    sentence_vectors = []
    for sentence in russian_sentences:
        vec = torch.tensor(nlp(sentence)).mean(dim=1).numpy().flatten()
        if vec.ndim == 1:
            sentence_vectors.append(vec)
        else:
            print(f"Skipping sentence due to incorrect vector shape: {sentence}")

    if len(sentence_vectors) == 0:
        return jsonify({"summary": "Failed to vectorize sentences."})

    sentence_vectors = np.array(sentence_vectors)
    print(f"Shape of sentence_vectors: {sentence_vectors.shape}")

    dimension = sentence_vectors.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(sentence_vectors)

    # Query vector
    query_vector = torch.tensor(nlp(query)).mean(dim=1).numpy().flatten().reshape(1, -1)
    print(f"Query vector shape: {query_vector.shape}")

    # Search in FAISS index
    k = 10  # number of top relevant results to retrieve
    distances, indices = index.search(query_vector, k)
    relevant_snippets = [russian_sentences[i] for i in indices[0]]

    # Ensure unique and non-similar snippets
    unique_snippets = list(dict.fromkeys(relevant_snippets))
    filtered_snippets = []
    for snippet in unique_snippets:
        if not any(difflib.SequenceMatcher(None, snippet, filtered_snippet).ratio() > 0.7 for filtered_snippet in filtered_snippets):
            filtered_snippets.append(snippet)

    # Create summary from the most relevant snippet
    if filtered_snippets:
        summary = create_summary(filtered_snippets[0], max_length=100, min_length=30)
        print("Summary:", summary)
    else:
        summary = "No relevant summary could be generated."

    return jsonify({"summary": summary})

def create_summary(text, max_length=100, min_length=30):
    if len(word_tokenize(text)) < min_length:
        return text  # If the text is shorter than the minimum length, return it as is

    max_chunk = 512  # Adjusted maximum length of text chunk for summarization
    text_chunks = [text[i:i + max_chunk] for i in range(0, len(text), max_chunk)]
    
    summarized_texts = []
    for chunk in text_chunks:
        chunk_length = len(word_tokenize(chunk))
        print(f"Summarizing chunk: {chunk[:200]}...")  # Log the first part of the text chunk

        # Dynamically adjust max_length based on chunk length
        adjusted_max_length = min(max_length, chunk_length)
        summarized_text = summarizer(chunk, max_length=adjusted_max_length, min_length=min_length, do_sample=False)
        summarized_texts.append(summarized_text[0]['summary_text'])
    
    summary = " ".join(summarized_texts)
    if len(word_tokenize(summary)) > max_length:
        summary = " ".join(word_tokenize(summary)[:max_length])
    return summary

if __name__ == '__main__':
    app.run(debug=True, port=5000)

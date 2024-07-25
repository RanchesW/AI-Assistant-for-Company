import docx
import tkinter as tk
from tkinter import filedialog, messagebox
from nltk.tokenize import PunktSentenceTokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Функции для обработки Word
def extract_text_from_docx(file):
    doc = docx.Document(file)
    text = []
    for paragraph in doc.paragraphs:
        text.append(paragraph.text)
    return ' '.join(text)

def answer_question(doc_text, question):
    # Используем кастомный токенизатор с учетом сокращений
    custom_tokenizer = PunktSentenceTokenizer()
    custom_tokenizer._params.abbrev_types.add('эл')
    sentences = custom_tokenizer.tokenize(doc_text)
    
    tfidf_vectorizer = TfidfVectorizer().fit_transform(sentences)
    question_vec = TfidfVectorizer().fit(sentences).transform([question])
    similarities = cosine_similarity(question_vec, tfidf_vectorizer).flatten()
    best_match_index = np.argmax(similarities)
    return sentences[best_match_index]

# GUI функции
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Анализ Word документов")

        self.file_label = tk.Label(root, text="Выберите файл Word:")
        self.file_label.grid(row=0, column=0, padx=10, pady=5)

        self.file_path = tk.Entry(root, width=50)
        self.file_path.grid(row=0, column=1, padx=10, pady=5)

        self.file_button = tk.Button(root, text="Обзор...", command=self.load_file)
        self.file_button.grid(row=0, column=2, padx=10, pady=5)

        self.question_label = tk.Label(root, text="Введите вопрос:")
        self.question_label.grid(row=1, column=0, padx=10, pady=5)

        self.question_entry = tk.Entry(root, width=50)
        self.question_entry.grid(row=1, column=1, padx=10, pady=5)

        self.run_button = tk.Button(root, text="Запуск", command=self.run_action)
        self.run_button.grid(row=2, column=1, pady=10)

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Word files", "*.docx"), ("All files", "*.*")])
        self.file_path.delete(0, tk.END)
        self.file_path.insert(0, file_path)

    def run_action(self):
        file = self.file_path.get()
        question = self.question_entry.get()
        doc_text = extract_text_from_docx(file)
        answer = answer_question(doc_text, question)
        self.show_result(answer)

    def show_result(self, result_text):
        self.result_text = result_text
        result_window = tk.Toplevel(self.root)
        result_window.title("Результат")
        result_text_widget = tk.Text(result_window, wrap="word")
        result_text_widget.pack(expand=True, fill='both')
        result_text_widget.insert('1.0', result_text)
        result_text_widget.config(state=tk.DISABLED)

        save_button = tk.Button(result_window, text="Сохранить в файл", command=self.save_result)
        save_button.pack(pady=10)

    def save_result(self):
        save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if save_path:
            with open(save_path, 'w', encoding='utf-8') as f:
                f.write(self.result_text)
            messagebox.showinfo("Успех", f"Результат успешно сохранен в {save_path}")

root = tk.Tk()
app = App(root)
root.mainloop()

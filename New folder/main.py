from flask import Flask, request, jsonify, render_template
import pandas as pd
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'xlsx', 'xls', 'csv'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        return jsonify({'message': 'File uploaded successfully', 'filename': filename}), 200

    return jsonify({'error': 'Invalid file type'}), 400

@app.route('/sheets', methods=['GET'])
def get_sheets():
    filename = request.args.get('filename')
    if not filename or not allowed_file(filename):
        return jsonify({'error': 'Invalid filename'}), 400

    try:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        xls = pd.ExcelFile(filepath)
        sheets = xls.sheet_names
        return jsonify({'sheets': sheets}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/select_sheet', methods=['POST'])
def select_sheet():
    data = request.get_json()
    filename = data.get('filename')
    sheet_name = data.get('sheet_name')
    date_column = data.get('date_column')
    comparison_column = data.get('comparison_column')

    if not filename or not allowed_file(filename):
        return jsonify({'error': 'Invalid filename'}), 400

    try:
        # Загрузка данных из выбранного листа
        df = pd.read_excel(os.path.join(app.config['UPLOAD_FOLDER'], filename), sheet_name=sheet_name)

        # Дополнительная обработка данных
        df[date_column] = pd.to_datetime(df[date_column], errors='coerce')
        df['Year'] = df[date_column].dt.year
        df['Month'] = df[date_column].dt.month

        unique_years = df['Year'].dropna().unique().tolist()
        unique_months = df['Month'].dropna().unique().tolist()
        return jsonify({'years': unique_years, 'months': unique_months, 'columns': df.columns.tolist()}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/available_dates', methods=['GET'])
def get_available_dates():
    filename = request.args.get('filename')
    sheet_name = request.args.get('sheet_name')
    date_column = request.args.get('date_column')
    if not filename or not allowed_file(filename):
        return jsonify({'error': 'Invalid filename'}), 400

    try:
        df = pd.read_excel(os.path.join(app.config['UPLOAD_FOLDER'], filename), sheet_name=sheet_name)
        if date_column not in df.columns:
            return jsonify({'error': 'Date column not found'}), 400

        df[date_column] = pd.to_datetime(df[date_column], errors='coerce')
        df['Year'] = df[date_column].dt.year
        df['Month'] = df[date_column].dt.month
        unique_years = df['Year'].dropna().unique().tolist()
        unique_months = df['Month'].dropna().unique().tolist()
        return jsonify({'years': unique_years, 'months': unique_months}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/compare_data', methods=['POST'])
def compare_data():
    data = request.get_json()
    filename = data.get('filename')
    sheet_name = data.get('sheet_name')
    date_column = data.get('date_column')
    selected_years = data.get('years', [])
    selected_months = data.get('months', [])
    comparison_column = data.get('comparison_column')

    if not filename or not allowed_file(filename):
        return jsonify({'error': 'Invalid filename'}), 400

    try:
        df = pd.read_excel(os.path.join(app.config['UPLOAD_FOLDER'], filename), sheet_name=sheet_name)
        df[date_column] = pd.to_datetime(df[date_column], errors='coerce')
        df['Year'] = df[date_column].dt.year
        df['Month'] = df[date_column].dt.month

        if selected_years:
            df = df[df['Year'].isin(selected_years)]
        if selected_months:
            df = df[df['Month'].isin(selected_months)]

        if comparison_column not in df.columns:
            return jsonify({'error': 'Comparison column not found'}), 400

        comparison_data = df.groupby(['Year', 'Month'])[comparison_column].mean().to_dict()
        return jsonify({'comparison_data': comparison_data}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)

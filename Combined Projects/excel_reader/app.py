import pandas as pd
from tkinter import Tk, Label, Button, Entry, filedialog, StringVar, OptionMenu
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Убедитесь, что необходимые пакеты загружены
# import nltk
# nltk.download('punkt')
# nltk.download('stopwords')

def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
    if file_path:
        file_path_var.set(file_path)
        load_sheet_names(file_path)

def load_sheet_names(file_path):
    xls = pd.ExcelFile(file_path)
    sheet_names_var.set(xls.sheet_names[0])
    sheet_menu['menu'].delete(0, 'end')
    for sheet in xls.sheet_names:
        sheet_menu['menu'].add_command(label=sheet, command=lambda value=sheet: sheet_names_var.set(value))

def analyze():
    file_path = file_path_var.get()
    sheet_name = sheet_names_var.get()
    user_query = section_entry.get().lower()

    # Загрузка данных из выбранного листа Excel
    df = pd.read_excel(file_path, sheet_name=sheet_name)

    # Токенизация и удаление стоп-слов
    tokens = word_tokenize(user_query)
    filtered_tokens = [word for word in tokens if word not in stopwords.words('russian')]
    
    # Поиск ключевых слов для выбора метода анализа
    if "бюджетный период" in user_query:
        analyze_budget_period(df, filtered_tokens)
    else:
        analyze_standard(df, filtered_tokens)

def analyze_standard(df, filtered_tokens):
    # Анализ стандартных данных (на примере Денежных средств)
    section_keyword = None
    for word in filtered_tokens:
        matching_rows = df[df.iloc[:, 0].str.contains(word, case=False, na=False)]
        if not matching_rows.empty:
            section_keyword = word
            break

    if section_keyword:
        section_row = matching_rows.index[0]
        starting_value = df.iloc[section_row, 1]
        ending_value = df.iloc[section_row, 2]
        difference = ending_value - starting_value
        percentage_change = (difference / starting_value) * 100

        result_label.config(text=f"На начало: {starting_value}\nНа конец: {ending_value}\nРазница: {difference}\nПроцентное изменение: {percentage_change:.2f}%")
    else:
        result_label.config(text="Не удалось найти ключевое слово для анализа.")

def analyze_budget_period(df, filtered_tokens):
    # Анализ данных по бюджетным периодам
    section_keyword = None
    for word in filtered_tokens:
        matching_rows = df[df.iloc[:, 0].str.contains(word, case=False, na=False)]
        if not matching_rows.empty:
            section_keyword = word
            break

    if section_keyword:
        section_row = matching_rows.index[0]
        periods = df.columns[1:-1]  # Предполагаем, что периоды находятся между первым и последним столбцами
        results = {}
        for period in periods:
            results[period] = df.at[section_row, period]

        result_text = "\n".join([f"Период {period}: {value}" for period, value in results.items()])
        result_label.config(text=result_text)
    else:
        result_label.config(text="Не удалось найти ключевое слово для анализа.")

root = Tk()
root.title("Анализ Excel данных")

# Variables
file_path_var = StringVar()
sheet_names_var = StringVar()
section_entry = Entry(root, width=30)

# Widgets
load_button = Button(root, text="Загрузить файл", command=load_file)
file_label = Label(root, text="Файл:")
file_path_label = Label(root, textvariable=file_path_var)
sheet_label = Label(root, text="Лист:")
sheet_menu = OptionMenu(root, sheet_names_var, "")
section_label = Label(root, text="Введите запрос:")
analyze_button = Button(root, text="Анализировать", command=analyze)
result_label = Label(root, text="", justify="left")

# Layout
load_button.grid(row=0, column=0, padx=10, pady=5)
file_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
file_path_label.grid(row=1, column=1, padx=10, pady=5)
sheet_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
sheet_menu.grid(row=2, column=1, padx=10, pady=5)
section_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
section_entry.grid(row=3, column=1, padx=10, pady=5)
analyze_button.grid(row=4, column=0, columnspan=2, pady=10)
result_label.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()

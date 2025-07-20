import csv

def read_financial_operations(file_path):
    transactions = []
    with open(file_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            transactions.append(row)
    return transactions


import pandas as pd

def read_financial_operations(file_path):
    # Считываем данные из Excel файла
    df = pd.read_excel(file_path)

    # Преобразуем DataFrame в список словарей
    transactions = df.to_dict(orient='records')

    return transactions

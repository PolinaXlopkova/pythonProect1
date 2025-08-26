import csv
import pandas as pd


def read_financial_operations(file_path):
    """
    Читает финансовые операции из CSV файла.

    Параметры:
    file_path (str): Путь к CSV файлу, содержащему финансовые операции.

    Возвращает:
    list: Список словарей, где каждый словарь представляет собой строку
    из CSV файла с именами столбцов в качестве ключей.
    """
    transactions = []
    with open(file_path, mode="r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            transactions.append(row)
    return transactions


def read_financial_operationss(file_path):
    """
    Считывает финансовые операции из Excel файла.

    Параметры:
        file_path (str): Путь к Excel файлу, содержащему финансовые операции.

    Возвращает:
        list: Список словарей, каждый из которых представляет финансовую операцию.
              Ключи словаря соответствуют именам столбцов в Excel файле.
    """
    # Считываем данные из Excel файла
    df = pd.read_excel(file_path)

    # Преобразуем DataFrame в список словарей
    transactions = df.to_dict(orient="records")

    return transactions

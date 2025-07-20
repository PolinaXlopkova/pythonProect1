import csv
import unittest
from unittest.mock import mock_open, patch
import pandas as pd


def read_financial_operations(file_path):
    transactions = []
    with open(file_path, mode="r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            transactions.append(row)
    return transactions


class TestReadFinancialOperations(unittest.TestCase):

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data="date,amount,description\n2023-01-01,100,Income\n2023-01-02,-50,Expense\n",
    )
    def test_read_financial_operations(self, mock_file):
        expected_result = [
            {"date": "2023-01-01", "amount": "100", "description": "Income"},
            {"date": "2023-01-02", "amount": "-50", "description": "Expense"},
        ]
        result = read_financial_operations("dummy_path.csv")
        self.assertEqual(result, expected_result)
        mock_file.assert_called_once_with("dummy_path.csv", mode="r", encoding="utf-8")


if __name__ == "__main__":
    unittest.main()

    @patch("pandas.read_excel")
    def test_read_financial_operations(self, mock_read_excel):
        # Подготовка данных для теста
        mock_data = {
            "Date": ["2023-01-01", "2023-01-02"],
            "Amount": [100.0, 200.0],
            "Description": ["Deposit", "Withdrawal"],
        }
        mock_df = pd.DataFrame(mock_data)
        mock_read_excel.return_value = mock_df

        # Вызов функции
        result = read_financial_operations("dummy_path.xlsx")

        # Ожидаемый результат
        expected_result = [
            {"Date": "2023-01-01", "Amount": 100.0, "Description": "Deposit"},
            {"Date": "2023-01-02", "Amount": 200.0, "Description": "Withdrawal"},
        ]

        # Проверка результата
        self.assertEqual(result, expected_result)
        mock_read_excel.assert_called_once_with("dummy_path.xlsx")


if __name__ == "__main__":
    unittest.main()

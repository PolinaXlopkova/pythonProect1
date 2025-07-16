import unittest
import json
import os

from src.utils import load_transactions

class TestLoadTransactions(unittest.TestCase):

    def setUp(self):
        self.valid_file = 'test_valid.json'
        self.invalid_file = 'test_invalid.json'
        self.empty_file = 'test_empty.json'
        self.nonexistent_file = 'nonexistent.json'

        # Создаем файл с корректными данными
        with open(self.valid_file, 'w') as f:
            json.dump([{"amount": 100, "currency": "USD"}, {"amount": 200, "currency": "EUR"}], f)

        # Создаем файл с некорректными данными
        with open(self.invalid_file, 'w') as f:
            f.write("Not a JSON")

        # Создаем пустой файл
        open(self.empty_file, 'w').close()

    def tearDown(self):
        # Удаляем созданные файлы после тестов
        for file in [self.valid_file, self.invalid_file, self.empty_file]:
            if os.path.exists(file):
                os.remove(file)

    def test_load_valid_transactions(self):
        result = load_transactions(self.valid_file)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['amount'], 100)
        self.assertEqual(result[1]['currency'], 'EUR')

    def test_load_invalid_json(self):
        result = load_transactions(self.invalid_file)
        self.assertEqual(result, [])

    def test_load_empty_file(self):
        result = load_transactions(self.empty_file)
        self.assertEqual(result, [])

    def test_load_nonexistent_file(self):
        result = load_transactions(self.nonexistent_file)
        self.assertEqual(result, [])

    def test_load_non_list_json(self):
        with open('test_non_list.json', 'w') as f:
            json.dump({"amount": 100}, f)
        result = load_transactions('test_non_list.json')
        self.assertEqual(result, [])
        os.remove('test_non_list.json')

if __name__ == '__main__':
    unittest.main()
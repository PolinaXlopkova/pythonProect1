import unittest
from unittest.mock import patch
from src.external_api import convert_to_rub

class TestCurrencyConversion(unittest.TestCase):

    @patch('src.external_api.get_exchange_rate')
    def test_convert_usd_to_rub(self, mock_get_exchange_rate):
        mock_get_exchange_rate.return_value = 75.0  # Пример курса USD к RUB
        transaction = {'amount': 100, 'currency': 'USD'}
        result = convert_to_rub(transaction)
        self.assertEqual(result, 7500.0)  # 100 * 75 = 7500

    @patch('src.external_api.get_exchange_rate')
    def test_convert_eur_to_rub(self, mock_get_exchange_rate):
        mock_get_exchange_rate.return_value = 85.0  # Пример курса EUR к RUB
        transaction = {'amount': 100, 'currency': 'EUR'}
        result = convert_to_rub(transaction)
        self.assertEqual(result, 8500.0)  # 100 * 85 = 8500

    def test_convert_rub(self):
        transaction = {'amount': 100, 'currency': 'RUB'}
        result = convert_to_rub(transaction)
        self.assertEqual(result, 100.0)  # RUB остается без изменений

    def test_unsupported_currency(self):
        transaction = {'amount': 100, 'currency': 'GBP'}
        with self.assertRaises(ValueError) as context:
            convert_to_rub(transaction)
        self.assertEqual(str(context.exception), "Unsupported currency")

if __name__ == '__main__':
    unittest.main()

import requests
from dotenv import load_dotenv
import os

load_dotenv()

def get_exchange_rate(currency):
    url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency}&symbols=RUB"
    headers = {
        "apikey": os.getenv('API_KEY')
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return data['rates']['RUB']


def convert_to_rub(transaction):
    amount = transaction['amount']
    currency = transaction['currency']

    if currency == 'RUB':
        return float(amount)
    elif currency in ['USD', 'EUR']:
        rate = get_exchange_rate(currency)
        return float(amount) * rate
    else:
        raise ValueError("Unsupported currency")

print("Загрузка .env файла")
load_dotenv()
api_key = os.getenv('API_KEY')
if api_key is None:
    print("API_KEY не найдена")
else:
    print("API_KEY загружена успешно", api_key)

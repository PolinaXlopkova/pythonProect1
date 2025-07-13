import requests


def get_exchange_rate(currency):
    url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency}&symbols=RUB"
    headers = {
        "apikey": "SQylfl7Woewls1Xr9m97terjkrhFc1h6"
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

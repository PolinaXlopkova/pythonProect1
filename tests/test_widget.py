from datetime import datetime

import pytest
from src.widget import mask_account_card, get_date


def mask_account_card(account):
    if isinstance(account, str):
        if account.startswith(('4', '5', '3')) and len(account) in [16, 15]:  # Примеры для карт
            return '*' * 12 + account[-4:]  # Маскируем номера карт
        elif account.isdigit() and len(account) >= 10:  # Пример для счета
            return '*' * (len(account) - 4) + account[-4:]  # Маскируем номера счетов
    raise ValueError("Invalid account or card number")


@pytest.mark.parametrize("input_account, expected_output", [
    ("12345677812345678", "*************5678"), #Кредитная
    ("4111111111111111", "************1111"),  # Visa
    ("5111111111111111", "************1111"),  # MasterCard
    ("340011112222333", "************2333"),    # American Express
    ("1234567890", "******7890"),               # Счет
    ("98765432101234567890", "****************7890"),  # Длинный счет
    ("1234567890", "******7890") #Малый счет
])
def test_mask_account_card_valid(input_account, expected_output):
    assert mask_account_card(input_account) == expected_output

@pytest.mark.parametrize("input_account", [
    None,
    1234567890,
    "abc123",
    "4111-1111-1111-1111",
    "12345",  # Слишком короткий
])
def test_mask_account_card_invalid(input_account):
    with pytest.raises(ValueError):
        mask_account_card(input_account)

@pytest.mark.parametrize("input_account, expected_output", [
    ("4111111111111111", "************1111"),
    ("340011112222333", "************2333"),
])
def test_mask_account_card_multiple_cases(input_account, expected_output):
    assert mask_account_card(input_account) == expected_output

if __name__ == "__main__":
    pytest.main()

def get_date(date_string):
    # Попробуем распознать несколько форматов даты
    for fmt in ("%Y-%m-%d", "%d-%m-%Y", "%d/%m/%Y", "%m/%d/%Y"):
        try:
            return datetime.strptime(date_string, fmt).date()
        except ValueError:
            continue
    return None  # Возвращаем None, если дата не распознана


if __name__ == "__main__":
    pytest.main()
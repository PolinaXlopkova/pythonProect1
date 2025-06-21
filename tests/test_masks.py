import pytest
from src.masks import get_mask_card_number, get_mask_account

def test_get_mask_card_number():
    # Тестирование правильности маскирования номера карты
    assert get_mask_card_number("1234 5678 1234 5678") == "**** **** **** 5678"
    assert get_mask_card_number("1234 5678 9012 3456") == "**** **** **** 3456"
    assert get_mask_card_number("1234-5678-9012-3456") == "Ошибка: номер карты должен состоять только из цифры"
    assert get_mask_card_number("123456") == "Ошибка: номер карты должен содержать 16 цифр"
    assert get_mask_card_number("1") == "Ошибка: номер карты должен содержать 16 цифр"

    # Проверка работы с нестандартными длинами номеров
    assert get_mask_card_number("123456789012") == "Ошибка: номер карты должен содержать 16 цифр"
    assert get_mask_card_number("1234") == "Ошибка: номер карты должен содержать 16 цифр"

    # Проверка, что функция корректно обрабатывает отсутствующий номер карты
    assert get_mask_card_number("") == "Ошибка: номер карты должен состоять только из цифры"

    # Проверка, что функция обрабатывает нечисловые строки
    assert get_mask_card_number("abcd") == "Ошибка: номер карты должен состоять только из цифры"
    assert get_mask_card_number("1234abcd5678") == "Ошибка: номер карты должен состоять только из цифры"

def get_mask_account(account_number):
    # Проверка, что номер счета является строкой
    if not isinstance(account_number, str):
        raise ValueError("Номер счета должен быть строкой")

    # Проверка длины номера счета
    if len(account_number) < 4:
        return "Номер счета слишком короткий"

    # Маскируем все символы, кроме последних 4
    return '*' * (len(account_number) - 4) + account_number[-4:]

    # Тестирование функции
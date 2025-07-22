from logger import masks_logger


def get_mask_card_number(card_number):
    card_number = card_number.replace(" ", "")
    """Функция, которая маскирует номер банковской карты"""
    if not card_number.isdigit():
        return "Ошибка: номер карты должен состоять только из цифры"

    # Проверяем длину номера
    if len(card_number) != 16:
        return "Ошибка: номер карты должен содержать 16 цифр"

    masked_card_number = "**** **** **** " + card_number[-4:]
    return masked_card_number


def get_mask_account(account_number):
    """Функция, которая маскирует номер счета"""
    if not account_number.isdigit():
        return "Ошибка: номер карты должен состоять только из цифры"

    if len(account_number) < 4:
        return "Ошибка: номер счета должен содержать минимум 4 цифры"

    masked_number = "**{}".format(account_number[-4:])

    return masked_number


def some_function():
    masks_logger.info("Это информационное сообщение из masks.")

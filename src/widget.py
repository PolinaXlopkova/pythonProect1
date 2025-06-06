def mask_card_number(number: str) -> str:
    '''Маскирует все цифры карты, кроме последних 4'''
    return '*' * (len(number) - 4) + number[-4:]

def mask_account_number(number: str) -> str:
    '''Маскирует первые 6 и последние 4 цифры счета, показывая середину'''
    return number[:6] + '*' * (len(number) - 10) + number[-4:]

def mask_account_card(info: str) -> str:
    '''Разделяем строку по последнему пробелу (имя типа может иметь пробелы)'''
    last_space = info.rfind(' ')
    name = info[:last_space]
    number = info[last_space + 1:]

    '''Определяем тип (если начинается с "Счет", используем маску для счета)'''
    if name.startswith('Счет'):
        masked_number = mask_account_number(number)
    else:
        masked_number = mask_card_number(number)

    return f"{name} {masked_number}"
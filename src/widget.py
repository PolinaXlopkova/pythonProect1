def mask_card_number(number: str) -> str:
    '''Маскирует все цифры карты, кроме последних 4'''
    return '*' * (len(number) - 4) + number[-4:]

def mask_account_number(number: str) -> str:
    '''Маскирует первые 6 и последние 4 цифры счета, показывая середину'''
    return number[:6] + '*' * (len(number) - 10) + number[-4:]

def mask_account_card(info: str) -> str:
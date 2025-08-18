import re
from collections import Counter


def process_bank_operations(transactions, search_string):
    # Создаем регулярное выражение для поиска
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)

    # Фильтруем список словарей операций
    result = [transaction for transaction in transactions if pattern.search(transaction.get('description', ''))]

    return result


def process_bank_search(transactions, category_dict):
    # Подсчет транзакций по описанию
    transaction_counts = Counter()

    for transaction in transactions:
        # Предполагаем, что каждая транзакция имеет поле 'category'
        category = transaction.get('category')
        if category in category_dict:
            transaction_counts[category] += 1

    # Преобразуем счетчик в словарь
    return dict(transaction_counts)

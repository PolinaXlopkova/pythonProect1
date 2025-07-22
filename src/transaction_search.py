import re


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    # Компилируем регулярное выражение для поиска
    pattern = re.compile(re.escape(search), re.IGNORECASE)

    # Фильтруем список словарей по описанию
    result = [entry for entry in data if 'description' in entry and pattern.search(entry['description'])]

    return result


def process_bank_operations(data: list[dict], categories: list) -> dict:
    category_counts = {category: 0 for category in categories}

    for operation in data:
        description = operation.get('description')
        if description in category_counts:
            category_counts[description] += 1

    return category_counts

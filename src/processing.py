from datetime import datetime
from typing import Dict, List
 develop
feature/homework_10_1


feature/homework_13_2


 feature/homework_12_2
 main
feature/homework_12_2


develop
 develop
 develop



 main
 main
 develop
def filter_by_state(data: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Фильтрует список словарей по значению ключа 'state'"""
    filtered_data = []

    for item in data:
        if "state" in item and item["state"] == state:
            filtered_data.append(item)

    return filtered_data
 develop
feature/homework_10_1



 feature/homework_13_2


 feature/homework_12_2
 main
feature/homework_12_2


develop
 develop
 develop



 main
 main
 develop
def sort_by_date(operations: list, ascending: bool = False) -> list:
    """Сортирует список операций по дате."""

    def get_date(operation: dict) -> datetime:
        try:
            date_string: str = operation["date"]
            # Преобразуем строку в объект datetime для корректной сортировки
            return datetime.strptime(date_string, "%Y-%m-%d")
        except (KeyError, ValueError):
            raise ValueError("Некорректный формат даты или отсутствие ключа 'date'")

    # Сортируем список с использованием полученной функции get_date
 feature/homework_13_2
    return sorted(operations, key=get_date, reverse=not ascending)

 feature/homework_10_1
    return sorted(operations, key=get_date, reverse=not ascending)

 feature/homework_12_2
 feature/homework_12_2
    return sorted(operations, key=get_date, reverse=not ascending)

    return sorted(operations, key=get_date, reverse=not ascending)
 develop
 develop
develop


    return sorted(operations, key=get_date, reverse=not ascending)
 main
 main
 develop

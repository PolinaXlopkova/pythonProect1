import pytest
from src.processing import filter_by_state, sort_by_date
from datetime import datetime


def filter_byу_state(data, state):
    return [item for item in data if item.get("state") == state]


# Тестовые данные
test_data = [
    {"name": "Item 1", "state": "active"},
    {"name": "Item 2", "state": "inactive"},
    {"name": "Item 3", "state": "active"},
]


# Параметризация тестов
@pytest.mark.parametrize(
    "state, expected",
    [
        ("active", [{"name": "Item 1", "state": "active"}, {"name": "Item 3", "state": "active"}]),
        ("inactive", [{"name": "Item 2", "state": "inactive"}]),
        ("pending", []),  # Нет элементов с таким статусом
        ("", []),  # Пустая строка как статус
    ],
)
def test_filter_by_state(state, expected):
    assert filter_by_state(test_data, state) == expected


if __name__ == "__main__":
    pytest.main()


def sort_byу_date(data, ascending=True):
    try:
        return sorted(data, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%d"), reverse=not ascending)
    except (ValueError, KeyError):
        return []


# Тесты для функции
def test_sort_by_date_ascending():
    data = [{"date": "2023-10-01"}, {"date": "2023-09-01"}, {"date": "2023-11-01"}]
    sorted_data = sort_by_date(data, ascending=True)
    assert sorted_data == [{"date": "2023-09-01"}, {"date": "2023-10-01"}, {"date": "2023-11-01"}]


def test_sort_by_date_descending():
    data = [{"date": "2023-10-01"}, {"date": "2023-09-01"}, {"date": "2023-11-01"}]
    sorted_data = sort_by_date(data, ascending=False)
    assert sorted_data == [{"date": "2023-11-01"}, {"date": "2023-10-01"}, {"date": "2023-09-01"}]


def test_sort_by_date_with_same_dates():
    data = [{"date": "2023-10-01"}, {"date": "2023-10-01"}, {"date": "2023-09-01"}]
    sorted_data = sort_by_date(data, ascending=True)
    assert sorted_data == [{"date": "2023-09-01"}, {"date": "2023-10-01"}, {"date": "2023-10-01"}]


def test_sort_by_date_invalid_format():
    data = [{"date": "invalid-date"}, {"date": "2023-09-01"}]
    sorted_data = sort_by_date(data)
    assert sorted_data == []


def test_sort_by_date_missing_date_key():
    data = [{"not_date": "2023-10-01"}, {"date": "2023-09-01"}]
    sorted_data = sort_by_date(data)
    assert sorted_data == []


if __name__ == "__main__":
    pytest.main()

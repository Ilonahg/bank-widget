from src.processing import filter_by_state, sort_by_date


# Тест для filter_by_state
def test_filter_by_state():
    data = [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01T10:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2022-01-01T12:00:00"},
    ]
    result = filter_by_state(data, "EXECUTED")
    # Проверка, что фильтрация работает правильно
    assert result == [{"id": 1, "state": "EXECUTED", "date": "2023-01-01T10:00:00"}]


# Тест для sort_by_date
def test_sort_by_date_descending():
    data = [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01T10:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2022-01-01T12:00:00"},
    ]
    # Применение сортировки
    result = sort_by_date(data)
    # Ожидаемый результат — отсортированные данные по убыванию даты
    expected = [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01T10:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2022-01-01T12:00:00"},
    ]
    assert result == expected

    import pytest
    from src.processing import find_transactions_by_description, count_transactions_by_category

    # Пример данных для тестов
    transactions = [
        {"id": 1, "description": "Оплата товаров"},
        {"id": 2, "description": "Перевод на карту"},
        {"id": 3, "description": "Оплата товаров"},
        {"id": 4, "description": "Снятие наличных"},
    ]

    def test_find_transactions_by_description():
        result = find_transactions_by_description(transactions, "оплата")
        assert len(result) == 2
        assert result[0]["description"] == "Оплата товаров"

    def test_count_transactions_by_category():
        result = count_transactions_by_category(transactions)
        assert result["Оплата товаров"] == 2
        assert result["Перевод на карту"] == 1
        assert result["Снятие наличных"] == 1


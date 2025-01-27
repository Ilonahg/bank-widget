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

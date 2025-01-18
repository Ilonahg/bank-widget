from src.processing import filter_by_state, sort_by_date

def test_filter_by_state():
    data = [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01T10:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2022-01-01T12:00:00"},
    ]
    result = filter_by_state(data, "EXECUTED")
    assert result == [{"id": 1, "state": "EXECUTED", "date": "2023-01-01T10:00:00"}]

def test_sort_by_date_descending():
    data = [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01T10:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2022-01-01T12:00:00"},
    ]
    result = sort_by_date(data)
    expected = [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01T10:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2022-01-01T12:00:00"},
    ]
    assert result == expected

import pytest

from src.processing import filter_by_state, sort_by_date


# Фикстура для генерации тестовых данных
@pytest.fixture
def sample_data() -> list:
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01"},
        {"id": 2, "state": "CANCELED", "date": "2022-01-01"},
        {"id": 3, "state": "EXECUTED", "date": "2021-01-01"},
    ]


def test_filter_by_state(sample_data: list) -> None:
    result = filter_by_state(sample_data, state="EXECUTED")
    assert len(result) == 2
    assert all(item["state"] == "EXECUTED" for item in result)


@pytest.mark.parametrize("state, expected_count", [
    ("EXECUTED", 2),
    ("CANCELED", 1),
    ("PENDING", 0),
])
def test_filter_by_state_parametrized(sample_data: list, state: str, expected_count: int) -> None:
    result = filter_by_state(sample_data, state)
    assert len(result) == expected_count


def test_sort_by_date_default(sample_data: list) -> None:
    result = sort_by_date(sample_data)
    # Проверяем, что дата первого элемента самая свежая (по умолчанию)
    assert result[0]["date"] == "2023-01-01"


def test_sort_by_date_ascending(sample_data: list) -> None:
    result = sort_by_date(sample_data, descending=False)
    # Проверяем, что дата первого элемента самая старая (при сортировке по возрастанию)
    assert result[0]["date"] == "2021-01-01"


def test_sort_by_date_descending(sample_data: list) -> None:
    result = sort_by_date(sample_data, descending=True)
    # Проверяем, что дата первого элемента самая свежая (при сортировке по убыванию)
    assert result[0]["date"] == "2023-01-01"

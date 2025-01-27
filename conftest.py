import pytest


# Фикстуры для генерации тестовых данных
@pytest.fixture
def sample_data() -> list:
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01"},
        {"id": 2, "state": "CANCELED", "date": "2022-01-01"},
        {"id": 3, "state": "EXECUTED", "date": "2021-01-01"},
    ]

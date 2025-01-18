import pytest
from src.generators.generators import card_number_generator, filter_by_currency, transaction_descriptions

# Пример транзакций
transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "RUB", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160"
    }
]

# Тест для filter_by_currency с параметризацией
@pytest.mark.parametrize("currency, expected_count, expected_descriptions", [
    ("USD", 2, ["Перевод организации", "Перевод со счета на счет"]),
    ("RUB", 1, ["Перевод со счета на счет"]),
    ("EUR", 0, [])
])
def test_filter_by_currency(currency, expected_count, expected_descriptions):
    transactions_filtered = list(filter_by_currency(transactions, currency))
    assert len(transactions_filtered) == expected_count
    for i, description in enumerate(expected_descriptions):
        assert transactions_filtered[i]["description"] == description

# Тест для transaction_descriptions с параметризацией
@pytest.mark.parametrize("expected_descriptions", [
    (["Перевод организации", "Перевод со счета на счет", "Перевод со счета на счет"])
])
def test_transaction_descriptions(expected_descriptions):
    descriptions = list(transaction_descriptions(transactions))
    assert len(descriptions) == len(expected_descriptions)
    for i, description in enumerate(expected_descriptions):
        assert descriptions[i] == description

# Тест для card_number_generator с параметризацией
@pytest.mark.parametrize("start, stop, expected", [
    (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
    (5, 7, ["0000 0000 0000 0005", "0000 0000 0000 0006", "0000 0000 0000 0007"]),
    (10, 12, ["0000 0000 0000 0010", "0000 0000 0000 0011", "0000 0000 0000 0012"])
])
def test_card_number_generator(start, stop, expected):
    card_numbers = list(card_number_generator(start, stop))
    assert card_numbers == expected
import pytest
from src.generators.generators import card_number_generator, filter_by_currency, transaction_descriptions

# Пример транзакций
transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "RUB", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160"
    }
]

# Тест для filter_by_currency с параметризацией
@pytest.mark.parametrize("currency, expected_count, expected_descriptions", [
    ("USD", 2, ["Перевод организации", "Перевод со счета на счет"]),
    ("RUB", 1, ["Перевод со счета на счет"]),
    ("EUR", 0, [])
])
def test_filter_by_currency(currency, expected_count, expected_descriptions):
    transactions_filtered = list(filter_by_currency(transactions, currency))
    assert len(transactions_filtered) == expected_count
    for i, description in enumerate(expected_descriptions):
        assert transactions_filtered[i]["description"] == description

# Тест для transaction_descriptions с параметризацией
@pytest.mark.parametrize("expected_descriptions", [
    (["Перевод организации", "Перевод со счета на счет", "Перевод со счета на счет"])
])
def test_transaction_descriptions(expected_descriptions):
    descriptions = list(transaction_descriptions(transactions))
    assert len(descriptions) == len(expected_descriptions)
    for i, description in enumerate(expected_descriptions):
        assert descriptions[i] == description

# Тест для card_number_generator с параметризацией
@pytest.mark.parametrize("start, stop, expected", [
    (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
    (5, 7, ["0000 0000 0000 0005", "0000 0000 0000 0006", "0000 0000 0000 0007"]),
    (10, 12, ["0000 0000 0000 0010", "0000 0000 0000 0011", "0000 0000 0000 0012"])
])
def test_card_number_generator(start, stop, expected):
    card_numbers = list(card_number_generator(start, stop))
    assert card_numbers == expected

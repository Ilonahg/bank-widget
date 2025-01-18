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

# Тест для filter_by_currency
def test_filter_by_currency():
    usd_transactions = filter_by_currency(transactions, "USD")
    result = list(usd_transactions)
    assert len(result) == 2
    assert result[0]["description"] == "Перевод организации"
    assert result[1]["description"] == "Перевод со счета на счет"

# Тест для transaction_descriptions
def test_transaction_descriptions():
    descriptions = transaction_descriptions(transactions)
    result = list(descriptions)
    assert len(result) == 3
    assert result[0] == "Перевод организации"
    assert result[1] == "Перевод со счета на счет"
    assert result[2] == "Перевод со счета на счет"

# Тест для card_number_generator
@pytest.mark.parametrize("start, stop, expected", [
    (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
    (5, 7, ["0000 0000 0000 0005", "0000 0000 0000 0006", "0000 0000 0000 0007"])
])
def test_card_number_generator(start, stop, expected):
    card_numbers = list(card_number_generator(start, stop))
    assert card_numbers == expected

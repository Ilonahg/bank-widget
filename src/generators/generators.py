# src/generators/generators.py

from typing import Dict, Iterator, List


# Функция filter_by_currency фильтрует транзакции по валюте
def filter_by_currency(transactions: List[Dict], currency: str) -> Iterator[Dict]:
    """
    Фильтрует транзакции по валюте.

    :param transactions: Список транзакций.
    :param currency: Валюта, по которой нужно фильтровать.
    :return: Итератор, который возвращает транзакции с заданной валютой.
    """
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


# Генератор transaction_descriptions возвращает описание транзакции
def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """
    Генератор для описания транзакций.

    :param transactions: Список транзакций.
    :return: Итератор, который поочередно возвращает описание транзакции.
    """
    for transaction in transactions:
        yield transaction["description"]


# Генератор card_number_generator генерирует номера карт в заданном диапазоне
def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генерирует номера карт в формате XXXX XXXX XXXX XXXX в заданном диапазоне.

    :param start: Начальное значение генерации.
    :param stop: Конечное значение генерации.
    :return: Итератор, который генерирует номера карт в заданном диапазоне.
    """
    for i in range(start, stop + 1):
        # Форматируем номер карты в виде XXXX XXXX XXXX XXXX
        card_number = f"{i:016d}"
        formatted_card_number = ' '.join([card_number[i:i + 4] for i in range(0, 16, 4)])
        yield formatted_card_number

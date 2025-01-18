# src/processing.py
from typing import Dict, List


def filter_by_state(data: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """
    Фильтрует список операций по состоянию.

    Аргументы:
        data (List[Dict]): Список словарей, представляющих операции.
        state (str): Состояние, по которому нужно фильтровать (по умолчанию 'EXECUTED').

    Возвращает:
        List[Dict]: Новый список словарей с операциями, у которых состояние совпадает с переданным значением.
    """
    return [entry for entry in data if entry['state'] == state]


def sort_by_date(data: List[Dict], descending: bool = True) -> List[Dict]:
    """
    Сортирует список операций по дате.

    Аргументы:
        data (List[Dict]): Список словарей, представляющих операции.
        descending (bool): Параметр, определяющий порядок сортировки. По умолчанию True (сортировка по убыванию).

    Возвращает:
        List[Dict]: Новый отсортированный список операций.
    """
    return sorted(data, key=lambda x: x['date'], reverse=descending)

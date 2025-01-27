import json
from typing import Dict, List


def read_json_file(file_path: str) -> List[Dict]:
    """
    Читает JSON-файл и возвращает список словарей с данными о транзакциях.

    :param file_path: Путь к JSON-файлу
    :return: Список словарей с данными или пустой список при ошибке
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    return []

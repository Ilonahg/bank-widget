import json


def read_json_file(file_path):
    """
    Читає JSON файл та повертає список словників з фінансовими операціями.

    Параметри:
        file_path (str): Шлях до файлу JSON.

    Повертає:
        list: Список транзакцій, якщо файл успішно прочитано, інакше порожній список.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []

import json
import logging
from typing import Dict, List

# Создаем объект логгера для модуля utils
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Создаем обработчик, который записывает логи в файл logs/utils.log
file_handler = logging.FileHandler('logs/utils.log')
file_handler.setLevel(logging.DEBUG)

# Форматер для логов
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Добавляем обработчик в логгер
logger.addHandler(file_handler)


def read_json_file(file_path: str) -> List[Dict]:
    """
    Читает JSON-файл и возвращает список словарей с данными о транзакциях.

    :param file_path: Путь к JSON-файлу
    :return: Список словарей с данными или пустой список при ошибке
    """
    try:
        logger.debug(f'Попытка открыть файл: {file_path}')
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.info(f'Файл {file_path} успешно прочитан, загружено {len(data)} записей.')
                return data
            else:
                logger.error(f'Файл {file_path} не содержит список данных.')
    except FileNotFoundError:
        logger.error(f'Файл {file_path} не найден.')
    except json.JSONDecodeError:
        logger.error(f'Ошибка декодирования JSON в файле {file_path}.')
    return []

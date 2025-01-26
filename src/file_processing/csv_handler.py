import csv
import logging
from typing import Dict, List

# Настройка логирования
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('logs/csv_handler.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def read_csv_file(file_path: str) -> List[Dict]:
    """
    Считывает финансовые транзакции из CSV-файла.

    :param file_path: Путь к файлу CSV
    :return: Список словарей с транзакциями или пустой список при ошибке
    """
    try:
        logger.debug(f'Попытка открыть файл: {file_path}')
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            transactions = [row for row in reader]
            logger.info(f'Успешно прочитано {len(transactions)} записей из файла {file_path}')
            return transactions
    except FileNotFoundError:
        logger.error(f'Файл {file_path} не найден.')
    except Exception as e:
        logger.error(f'Ошибка при чтении CSV файла: {e}')
    return []

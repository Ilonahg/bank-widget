import logging
from typing import Dict, List

import pandas as pd

# Настройка логирования
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('logs/excel_handler.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def read_excel_file(file_path: str) -> List[Dict]:
    """
    Считывает финансовые транзакции из Excel-файла.

    :param file_path: Путь к файлу XLSX
    :return: Список словарей с транзакциями или пустой список при ошибке
    """
    try:
        logger.debug(f'Попытка открыть файл: {file_path}')
        df = pd.read_excel(file_path)
        transactions = df.to_dict(orient='records')
        logger.info(f'Успешно прочитано {len(transactions)} записей из файла {file_path}')
        return transactions
    except FileNotFoundError:
        logger.error(f'Файл {file_path} не найден.')
    except Exception as e:
        logger.error(f'Ошибка при чтении Excel файла: {e}')
    return []

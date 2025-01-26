import os
import requests
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

API_KEY = os.getenv('EXCHANGE_API_KEY')
EXCHANGE_URL = 'https://api.apilayer.com/exchangerates_data/latest'

def convert_to_rub(transaction: dict) -> float:
    """
    Конвертирует сумму транзакции в рубли (RUB).

    :param transaction: Словарь с данными о транзакции
    :return: Сумма в рублях (float)
    """
    amount = transaction.get('amount', 0.0)
    currency = transaction.get('currency', 'RUB')

    if currency == 'RUB':
        return float(amount)

    params = {
        'access_key': API_KEY,
        'base': currency,
        'symbols': 'RUB'
    }

    try:
        response = requests.get(EXCHANGE_URL, params=params)
        response.raise_for_status()
        rates = response.json().get('rates', {})
        rub_rate = rates.get('RUB', 1.0)

        return float(amount) * rub_rate

    except requests.RequestException:
        return 0.0

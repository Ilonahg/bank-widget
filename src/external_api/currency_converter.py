import os
import requests
from dotenv import load_dotenv

# Завантаження змінних середовища з файлу .env
load_dotenv()

API_KEY = os.getenv("API_KEY")


def convert_to_rubles(transaction):
    """
    Конвертує суму транзакції з валюти (USD або EUR) в рублі.

    Параметри:
        transaction (dict): Словник з даними про транзакцію, що містить ключі 'amount' і 'currency'.

    Повертає:
        float: Сума транзакції в рублях.
    """
    amount = transaction['amount']
    currency = transaction['currency']

    if currency == 'RUB':
        return amount

    url = f'https://api.exchangeratesapi.io/latest?base={currency}&symbols=RUB&access_key={API_KEY}'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Якщо статус код не 2xx, піднімемо помилку
        data = response.json()
        return amount * data['rates']['RUB']
    except (requests.exceptions.RequestException, KeyError):
        return amount

# bank-widget
# Banking Widget

## Описание
Проект включает функции для обработки данных о банковских операциях.

## Установка
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ваше_имя_на_github/banking-widget.git
## Тестирование
Для запуска тестов используйте команду:
pytest

Все тесты должны пройти успешно. Для проверки покрытия используйте команду:
pytest --cov=src --cov-report=html

# Проект обработки транзакций

## Модуль generators

### Функции

1. **filter_by_currency(transactions: List[Dict], currency: str) -> Iterator[Dict]**
   Функция фильтрует список транзакций по валюте.

   Пример использования:
   ```python
   usd_transactions = filter_by_currency(transactions, "USD")
   for transaction in usd_transactions:
       print(transaction)

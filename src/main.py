import json
from processing import count_transactions_by_category, find_transactions_by_description


def load_transactions(file_path):
    """Загружает транзакции из JSON-файла."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Файл не найден. Попробуйте снова.")
        return None


def filter_transactions_by_status(transactions, status):
    """Фильтрует транзакции по заданному статусу."""
    return [tx for tx in transactions if tx.get("status") == status]


def main():
    """Основная функция программы, обрабатывающая банковские транзакции."""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")

    choice = input("Ваш выбор: ")
    if choice == "1":
        file_path = input("Введите путь к JSON-файлу: ")
        transactions = load_transactions(file_path)

        if transactions is None:
            return

        # Фильтрация по статусу операции
        status_filter = input("Введите статус транзакции для фильтрации (например, 'completed', 'pending'): ")
        transactions = filter_transactions_by_status(transactions, status_filter)

        if not transactions:
            print("Нет транзакций с указанным статусом.")
            return

        # Поиск по описанию
        search_str = input("Введите строку для поиска в описании транзакций: ")
        filtered_transactions = find_transactions_by_description(transactions, search_str)

        if not filtered_transactions:
            print("Не найдено транзакций, соответствующих вашему запросу.")
        else:
            print("Результаты поиска:")
            for transaction in filtered_transactions:
                print(transaction)

        # Подсчет количества операций по категориям
        print("\nПодсчёт количества операций по категориям:")
        category_count = count_transactions_by_category(transactions)
        for category, count in category_count.items():
            print(f"{category}: {count}")


if __name__ == "__main__":
    main()

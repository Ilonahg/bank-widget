import json

from processing import count_transactions_by_category, find_transactions_by_description


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")

    choice = input("Ваш выбор: ")
    if choice == "1":
        file_path = input("Введите путь к JSON-файлу: ")
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                transactions = json.load(file)
        except FileNotFoundError:
            print("Файл не найден. Попробуйте снова.")
            return

        print("Введите строку для поиска в описании транзакций:")
        search_str = input("> ")
        filtered_transactions = find_transactions_by_description(transactions, search_str)

        if not filtered_transactions:
            print("Не найдено транзакций, соответствующих вашему запросу.")
        else:
            print("Результаты поиска:")
            for transaction in filtered_transactions:
                print(transaction)

        print("\nПодсчёт количества операций по категориям:")
        category_count = count_transactions_by_category(transactions)
        for category, count in category_count.items():
            print(f"{category}: {count}")


if __name__ == "__main__":
    main()

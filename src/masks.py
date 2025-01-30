# src/masks.py

def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты.
    :param card_number: Номер карты в виде строки.
    :return: Маска номера карты в формате 'XXXX XX** **** XXXX' или сам номер, если его длина меньше 16.
    """
    # Проверка на некорректный ввод (должна быть строка с цифрами, длина хотя бы 4)
    if not card_number.isdigit() or len(card_number) < 4:
        raise ValueError("Некорректный номер карты. Ожидается строка с цифрами.")

    # Если длина номера меньше 16, то возвращаем без изменений
    if len(card_number) <= 4:
        return card_number

    # Возвращаем маску для обычного номера карты (16-значного)
    return f"{card_number[:4]} **** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счета.
    :param account_number: Номер счета в виде строки.
    :return: Маска номера счета в формате '******XXXX' или сам номер, если его длина меньше 6.
    """
    # Проверка на некорректный ввод (должна быть строка с цифрами, длина хотя бы 4)
    if not account_number.isdigit() or len(account_number) < 4:
        raise ValueError("Некорректный номер счета. Ожидается строка с цифрами.")

    # Если длина номера меньше или равна 6, возвращаем номер без изменений
    if len(account_number) <= 6:
        return account_number

    # Маска для обычных номеров счета
    return f"******{account_number[-4:]}"

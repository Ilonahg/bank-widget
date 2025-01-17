import re


def mask_account_card(card_info: str) -> str:
    """
    Функция для маскировки номера карты или счета.
    Принимает строку с типом карты и номером карты или счета.

    Возвращает строку с замаскированным номером.
    """
    # Регулярное выражение для разделения строки на тип карты и номер
    match = re.match(r"([A-Za-zА-Яа-я ]+) (\d+)", card_info)

    if not match:
        return "Неверный тип карты или счета"

    card_type = match.group(1).strip()  # Тип карты (например, "Visa Platinum")
    number = match.group(2)  # Номер карты или счета

    # Маскировка для карт
    if card_type in ['Visa', 'MasterCard', 'Maestro', 'Visa Platinum', 'Visa Classic', 'MasterCard World']:
        masked_number = f"{number[:4]} {number[4:6]}** **** {number[-4:]}"
    # Маскировка для счета
    elif card_type == 'Счет':
        masked_number = f"**{number[-4:]}"
    else:
        return "Неверный тип карты или счета"

    return f"{card_type} {masked_number}"


from datetime import datetime


def get_date(date_str: str) -> str:
    """
    Функция для преобразования строки с датой из формата
    "YYYY-MM-DDTHH:MM:SS.mmmmmm" в формат "DD.MM.YYYY".

    Параметры:
    date_str (str): строка с датой в формате "YYYY-MM-DDTHH:MM:SS.mmmmmm".

    Возвращает:
    str: дата в формате "DD.MM.YYYY".
    """
    # Преобразуем строку в объект datetime
    date_obj = datetime.fromisoformat(date_str.split('.')[0])  # игнорируем миллисекунды

    # Возвращаем дату в нужном формате
    return date_obj.strftime('%d.%m.%Y')


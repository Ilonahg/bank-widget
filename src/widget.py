from src.masks import get_mask_card_number, get_mask_account

def mask_account_card(data: str) -> str:
    """
    Masks account or card number based on its type.

    :param data: Input string in the format 'Type Number' (e.g., 'Visa Platinum 7000792289606361').
    :return: Masked string with appropriate masking.
    """
    if data.startswith("Счет"):
        number = data.split(" ", 1)[1]
        masked = get_mask_account(int(number))
        return f"Счет {masked}"
    else:
        type_name, number = data.rsplit(" ", 1)
        masked = get_mask_card_number(int(number))
        return f"{type_name} {masked}"


def get_date(date_string: str) -> str:
    """
    Converts a date string from ISO format to DD.MM.YYYY format.

    :param date_string: ISO date string (e.g., '2024-03-11T02:26:18.671407').
    :return: Date string in DD.MM.YYYY format (e.g., '11.03.2024').
    """
    from datetime import datetime
    date_obj = datetime.fromisoformat(date_string)
    return date_obj.strftime("%d.%m.%Y")

import pytest
from src.widget import mask_account_card, get_date

def test_mask_account_card():
    # Проверка маскировки номера карты
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"
    assert mask_account_card("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"
    assert mask_account_card("MasterCard 7158300734726758") == "MasterCard 7158 30** **** 6758"
    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"


def test_get_date():
    # Тестируем преобразование даты
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    assert get_date("2022-07-01T12:00:00.000000") == "01.07.2022"
    assert get_date("2018-12-25T00:00:00.000000") == "25.12.2018"

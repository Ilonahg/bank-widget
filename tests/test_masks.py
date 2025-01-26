import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number_valid() -> None:
    card_number = '1234567812345678'
    expected = '1234 **** **** 5678'
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_invalid() -> None:
    # Тест на некорректный номер карты (менее 4 цифр)
    with pytest.raises(ValueError):
        get_mask_card_number('123')  # Строка меньше 4 символов

    # Дополнительный тест на некорректный ввод (содержит не только цифры)
    with pytest.raises(ValueError):
        get_mask_card_number('1234abcd')  # Строка с буквами


def test_get_mask_account_valid() -> None:
    account_number = '1234567890123456'
    expected = '******3456'
    assert get_mask_account(account_number) == expected


def test_get_mask_account_invalid() -> None:
    # Тест на некорректный номер счета (менее 4 цифр)
    with pytest.raises(ValueError):
        get_mask_account('123')  # Строка меньше 4 символов

    # Дополнительный тест на некорректный ввод (содержит не только цифры)
    with pytest.raises(ValueError):
        get_mask_account('1234abcd')  # Строка с буквами


import pytest
from src.masks import mask_card_number

def test_mask_card_number_valid(caplog):
    result = mask_card_number("1234567812345678")
    assert result == "************5678"
    assert 'успешно замаскирована' in caplog.text

def test_mask_card_number_invalid(caplog):
    result = mask_card_number("123")
    assert result == "Invalid card number"
    assert 'Некорректный номер' in caplog.text

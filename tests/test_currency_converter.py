import pytest
from unittest.mock import patch
from src.external_api.currency_converter import convert_to_rubles

def test_convert_to_rubles_usd():
    transaction = {'amount': 100, 'currency': 'USD'}
    with patch('src.external_api.currency_converter.requests.get') as mock_get:
        mock_get.return_value.json.return_value = {'rates': {'RUB': 75.0}}
        result = convert_to_rubles(transaction)
        assert result == 7500.0
        mock_get.assert_called_once_with(
            'https://api.exchangeratesapi.io/latest?base=USD&symbols=RUB&access_key=your_api_key_here'
        )

def test_convert_to_rubles_eur():
    transaction = {'amount': 100, 'currency': 'EUR'}
    with patch('src.external_api.currency_converter.requests.get') as mock_get:
        mock_get.return_value.json.return_value = {'rates': {'RUB': 90.0}}
        result = convert_to_rubles(transaction)
        assert result == 9000.0
        mock_get.assert_called_once_with(
            'https://api.exchangeratesapi.io/latest?base=EUR&symbols=RUB&access_key=your_api_key_here'
        )

def test_convert_to_rubles_no_conversion():
    transaction = {'amount': 100, 'currency': 'RUB'}
    result = convert_to_rubles(transaction)
    assert result == 100.0

def test_convert_to_rubles_invalid_currency():
    transaction = {'amount': 100, 'currency': 'GBP'}
    result = convert_to_rubles(transaction)
    assert result == 100.0

def test_convert_to_rubles_api_error():
    transaction = {'amount': 100, 'currency': 'USD'}
    with patch('src.external_api.currency_converter.requests.get') as mock_get:
        mock_get.side_effect = Exception('API request failed')
        result = convert_to_rubles(transaction)
        assert result == 100.0

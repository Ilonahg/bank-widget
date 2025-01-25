import pytest
from unittest.mock import mock_open, patch
from src.utils.file_reader import read_json_file

def test_read_json_file_valid():
    # Проверка, если файл содержит корректный JSON (список)
    mock_file = mock_open(read_data='[{"amount": 100, "currency": "USD"}]')
    with patch('builtins.open', mock_file):
        result = read_json_file('test.json')
        assert result == [{"amount": 100, "currency": "USD"}]
        mock_file.assert_called_once_with('test.json', 'r', encoding='utf-8')

def test_read_json_file_empty():
    # Проверка пустого JSON файла
    mock_file = mock_open(read_data='[]')
    with patch('builtins.open', mock_file):
        result = read_json_file('empty.json')
        assert result == []
        mock_file.assert_called_once_with('empty.json', 'r', encoding='utf-8')
import pytest
from unittest.mock import mock_open, patch
from src.utils.file_reader import read_json_file

def test_read_json_file_valid():
    mock_file = mock_open(read_data='[{"amount": 100, "currency": "USD"}]')
    with patch('builtins.open', mock_file):
        result = read_json_file('test.json')
        assert result == [{"amount": 100, "currency": "USD"}]
        mock_file.assert_called_once_with('test.json', 'r', encoding='utf-8')

def test_read_json_file_empty():
    mock_file = mock_open(read_data='[]')
    with patch('builtins.open', mock_file):
        result = read_json_file('empty.json')
        assert result == []
        mock_file.assert_called_once_with('empty.json', 'r', encoding='utf-8')

def test_read_json_file_invalid_json():
    mock_file = mock_open(read_data='{"amount": 100, "currency": "USD"')
    with patch('builtins.open', mock_file):
        result = read_json_file('invalid.json')
        assert result == []
        mock_file.assert_called_once_with('invalid.json', 'r', encoding='utf-8')

def test_read_json_file_not_list():
    mock_file = mock_open(read_data='{"amount": 100, "currency": "USD"}')
    with patch('builtins.open', mock_file):
        result = read_json_file('not_a_list.json')
        assert result == []
        mock_file.assert_called_once_with('not_a_list.json', 'r', encoding='utf-8')

def test_read_json_file_not_found():
    with patch('builtins.open', side_effect=FileNotFoundError):
        result = read_json_file('not_found.json')
        assert result == []

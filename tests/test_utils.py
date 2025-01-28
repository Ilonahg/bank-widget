import pytest
import json
from unittest.mock import mock_open, patch
from src.utils import read_json_file


# Тест: Успешное чтение JSON-файла
def test_read_json_file_valid():
    mock_data = json.dumps([{"id": 1, "amount": 100}, {"id": 2, "amount": 200}])

    with patch("builtins.open", mock_open(read_data=mock_data)), \
            patch("json.load", return_value=json.loads(mock_data)):
        data = read_json_file("data/operations.json")

    assert isinstance(data, list)
    assert len(data) == 2
    assert data[0]["id"] == 1


# Тест: Файл не найден
def test_read_json_file_invalid():
    with patch("builtins.open", side_effect=FileNotFoundError):
        data = read_json_file("data/nonexistent.json")

    assert data == []


# Тест: Пустой JSON-файл
def test_read_json_file_empty():
    with patch("builtins.open", mock_open(read_data="")), \
            patch("json.load", side_effect=json.JSONDecodeError("Expecting value", "", 0)):
        data = read_json_file("data/empty.json")

    assert data == []

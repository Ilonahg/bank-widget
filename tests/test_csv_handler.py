import pytest
from src.file_processing.csv_handler import read_csv_file
from unittest.mock import mock_open, patch

# Мок CSV-данные
mock_csv_data = """date,amount,currency
2023-01-01,100,USD
2023-01-02,200,EUR
"""

@patch("builtins.open", new_callable=mock_open, read_data=mock_csv_data)
def test_read_csv_file(mock_file):
    result = read_csv_file("dummy_path.csv")
    assert len(result) == 2
    assert result[0]['amount'] == '100'

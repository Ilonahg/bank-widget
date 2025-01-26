import pytest
from src.file_processing.excel_handler import read_excel_file
import pandas as pd
from unittest.mock import patch

@patch("pandas.read_excel")
def test_read_excel_file(mock_read_excel):
    mock_read_excel.return_value = pd.DataFrame([
        {"date": "2023-01-01", "amount": 100, "currency": "USD"},
        {"date": "2023-01-02", "amount": 200, "currency": "EUR"}
    ])
    result = read_excel_file("dummy_path.xlsx")
    assert len(result) == 2
    assert result[1]["currency"] == "EUR"

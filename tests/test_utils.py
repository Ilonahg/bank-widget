import pytest
from src.utils import read_json_file

def test_read_json_file_valid():
    data = read_json_file('data/operations.json')
    assert isinstance(data, list)
    assert len(data) > 0

def test_read_json_file_invalid():
    data = read_json_file('data/nonexistent.json')
    assert data == []

def test_read_json_file_empty(tmp_path):
    temp_file = tmp_path / "empty.json"
    temp_file.write_text("")
    data = read_json_file(str(temp_file))
    assert data == []

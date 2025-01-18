import pytest
import logging
from src.decorators import log

# Фикстура для захвата логов
@pytest.fixture
def caplog(caplog):
    return caplog

# Тестирование успешного выполнения
@log
def add(x, y):
    return x + y

def test_log_success(caplog):
    add(1, 2)
    assert "Calling add with arguments: (1, 2), {}" in caplog.text
    assert "add ok: 3" in caplog.text

# Тестирование ошибки
@log
def divide(x, y):
    return x / y

def test_log_error(caplog):
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
    assert "divide error: division by zero. Inputs: (1, 0), {}" in caplog.text

# Тестирование с логированием в файл
@log(filename="test_log.txt")
def multiply(x, y):
    return x * y

def test_log_to_file():
    multiply(3, 4)
    with open("test_log.txt", "r") as f:
        log_content = f.read()
    assert "Calling multiply with arguments: (3, 4), {}" in log_content
    assert "multiply ok: 12" in log_content

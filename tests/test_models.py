import pytest
from src.models import Product, Category


def test_product_initialization():
    """Тест создания объекта Product."""
    product = Product("Тестовый продукт", "Описание", 100.0, 10)
    assert product.name == "Тестовый продукт"
    assert product.description == "Описание"
    assert product.price == 100.0
    assert product.quantity == 10


def test_category_initialization():
    """Тест создания объекта Category."""
    product1 = Product("Продукт 1", "Описание 1", 50.0, 5)
    product2 = Product("Продукт 2", "Описание 2", 75.0, 3)

    category = Category("Тестовая категория", "Описание категории", [product1, product2])
    assert category.name == "Тестовая категория"
    assert category.description == "Описание категории"
    assert len(category.products) == 2


def test_category_counters():
    """Тест подсчёта количества категорий и товаров."""
    Category.category_count = 0
    Category.product_count = 0

    product1 = Product("Продукт 1", "Описание 1", 50.0, 5)
    product2 = Product("Продукт 2", "Описание 2", 75.0, 3)
    product3 = Product("Продукт 3", "Описание 3", 100.0, 2)

    Category("Категория 1", "Описание 1", [product1, product2])
    Category("Категория 2", "Описание 2", [product3])

    assert Category.category_count == 2
    assert Category.product_count == 3

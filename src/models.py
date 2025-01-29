class Product:
    """Класс, представляющий товар."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализация товара.

        :param name: Название товара
        :param description: Описание товара
        :param price: Цена товара
        :param quantity: Количество на складе
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс, представляющий категорию товаров."""

    category_count = 0  # Количество категорий
    product_count = 0  # Количество товаров во всех категориях

    def __init__(self, name: str, description: str, products: list):
        """
        Инициализация категории.

        :param name: Название категории
        :param description: Описание категории
        :param products: Список товаров в категории (объекты класса Product)
        """
        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1  # Увеличиваем количество категорий
        Category.product_count += len(products)  # Увеличиваем общее количество товаров

from abc import ABC, abstractmethod


class Product:
    def __init__(self, name, price, description, quantity):
        self.name = name
        self.__price = price
        self.description = description
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(other, Product):
            return (self.price * self.quantity) + (other.price * other.quantity)
        return NotImplemented


class Category:
    product_count = 0
    category_count = 0

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
        self.__products = []
        Category.category_count += 1

    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            print("Можно добавлять только объекты класса Product или его наследников.")

    @property
    def products(self):
        return ''.join(
            [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n" for product in self.__products])

    @classmethod
    def new_product(cls, product_data):
        return Product(
            name=product_data['name'],
            price=product_data['price'],
            description=product_data['description'],
            quantity=product_data['quantity']
        )

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."


class LogCreationMixin:
    """Миксин для логирования создания объектов."""

    def init(self, *args, **kwargs):
        super().init(*args, **kwargs)
        self._log_creation()

    def _log_creation(self):
        """Логирует информацию о создании объекта."""
        class_name = self.__class__.name

        print(f"[LOG] Создан объект класса: {class_name}")


class BaseProduct(LogCreationMixin, ABC):
    """Абстрактный базовый класс для всех продуктов."""

    def init(self, name: str, description: str, price: float, quantity: int, **kwargs):
        # LogCreationMixin.init вызовется первым и напечатает логи
        super().init(name=name, description=description, price=price, quantity=quantity, **kwargs)

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @abstractmethod
    def get_additional_info(self) -> str:
        pass

    def str(self) -> str:
        return (f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.\n"
                f"Описание: {self.description}\n"
                f"{self.get_additional_info()}")

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print("Ошибка: Цена должна быть положительным числом.")
        elif new_price < self.__price:
            user_input = input(f"Новая цена ниже текущей. Подтвердите (y/n): ").strip().lower()
            if user_input == 'y':
                self.__price = new_price
        else:
            self.__price = new_price


# Классы-наследники остаются без изменений
class Smartphone(BaseProduct):
    def init(self, name: str, description: str, price: float, quantity: int,
             performance: float, model: str, memory: int, color: str):
        super().init(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color

    def get_additional_info(self) -> str:
        return (f"Характеристики: Модель - {self.model}, Цвет - {self.color}, "
                f"Память - {self.memory}ГБ, Производительность - {self.performance}ГГц")


class LawnGrass(BaseProduct):
    def init(self, name: str, description: str, price: float, quantity: int,
             country: str, germination_period: str, color: str):
        super().init(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def get_additional_info(self) -> str:
        return (f"Происхождение: {self.country}, "
                f"Срок прорастания - {self.germination_period}, "
                f"Цвет - {self.color}")

class BaseProduct(LogCreationMixin, ABC):
    """Абстрактный базовый класс для всех продуктов с функцией логирования."""

    def init(self, name: str, description: str, price: float, quantity: int, **kwargs):
        """
        Конструктор базового класса продукта.
        **kwargs нужен для передачи дополнительных аргументов в миксин и другие классы.
        """
        # Сохраняем аргументы для логирования перед передачей дальше
        self._init_args = {
            'name': name,
            'description': description,
            'price': price,
            'quantity': quantity
        }

        super().init(name=name, description=description, price=price, quantity=quantity, **kwargs)

        # Инициализация атрибутов
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


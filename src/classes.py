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


# Абстрактный класс BaseProduct
class BaseProduct(ABC):

    @abstractmethod
    def get_info(self):
        pass

# Класс Product, наследующийся от BaseProduct
class Product(BaseProduct):

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_info(self):
        return f'Product: {self.name}, Price: {self.price}'

# Класс Smartphone, наследующийся от Product
class Smartphone(Product):

    def __init__(self, name, price, model):
        super().__init__(name, price)
        self.model = model

    def get_info(self):
        return f'Smartphone: {self.name}, Model: {self.model}, Price: {self.price}'

# Класс LawnGrass, наследующийся от Product
class LawnGrass(Product):

    def __init__(self, name, price, type_of_grass):
        super().__init__(name, price)
        self.type_of_grass = type_of_grass

    def get_info(self):
        return f'LawnGrass: {self.name}, Type: {self.type_of_grass}, Price: {self.price}'

# Пример использования
smartphone = Smartphone("iPhone", 999, "12 Pro")
lawn_grass = LawnGrass("Kentucky Bluegrass", 50, "Cool-season")

print(smartphone.get_info())
print(lawn_grass.get_info())

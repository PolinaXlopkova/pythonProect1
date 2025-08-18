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
            print ("Цена не должна быть нулевая или отрицательная")


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

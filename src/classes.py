class Product:
    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

class Category:
    product_count = 0
    category_count = 0

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
        self.products = []
        Category.category_count += 1

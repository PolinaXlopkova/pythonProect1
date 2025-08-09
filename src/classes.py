class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Category:
    product_count = 0
    category_count = 0

    def __init__(self, name):
        self.name = name
        self.products = []
        Category.category_count += 1
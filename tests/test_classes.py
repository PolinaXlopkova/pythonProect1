from src.classes import Product, Category
import unittest

class TestProductAndCategory(unittest.TestCase):

    def test_category_initialization(self):
        # Проверка инициализации объекта Category
        category = Category("Electronics")
        self.assertEqual(category.name, "Electronics")
        self.assertEqual(Category.category_count, 1)

    def test_product_initialization(self):
        # Проверка инициализации объекта Product
        product = Product("Smartphone", 699.99)
        self.assertEqual(product.name, "Smartphone")
        self.assertEqual(product.price, 699.99)
        self.assertEqual(Category.product_count, 1)

    def test_multiple_categories(self):
        Category("Books")
        Category("Toys")
        self.assertEqual(Category.category_count, 3)

    def test_multiple_products(self):
        Product("Laptop", 999.99)
        Product("Tablet", 399.99)
        self.assertEqual(Category.product_count, 3)


if __name__ == '__main__':
    unittest.main()

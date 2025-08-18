from src.classes import Product, Category
import unittest
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestProductAndCategory(unittest.TestCase):

    def setUp(self):
        self.product1 = Product("Товар 1", 100, "Описание товара 1", 10)
        self.product2 = Product("Товар 2", 200, "Описание товара 2", 5)
        self.category = Category("Категория 1", 15)

    def test_product_initialization(self):
        self.assertEqual(self.product1.name, "Товар 1")
        self.assertEqual(self.product1.price, 100)
        self.assertEqual(self.product1.description, "Описание товара 1")
        self.assertEqual(self.product1.quantity, 10)

    def test_product_price_setter(self):
        # Исправлено: удален дублирующийся тест
        self.product1.price = 150
        self.assertEqual(self.product1.price, 150)

    def test_product_price_negative(self):
        with self.assertLogs(logger, level='INFO') as log:
            self.product1.price = -50
            self.assertIn("Цена не должна быть нулевая или отрицательная", log.output[0])

    def test_category_initialization(self):
        self.assertEqual(self.category.name, "Категория 1")
        self.assertEqual(self.category.quantity, 15)
        # Исправлено: правильное сравнение
        self.assertEqual(Category.category_count, 2)

    def test_add_product(self):
        self.category.add_product(self.product1)
        self.assertIn(self.product1, self.category._Category__products)
        self.assertEqual(Category.product_count, 1)

    def test_add_invalid_product(self):
        with self.assertLogs(logger, level='INFO') as log:
            self.category.add_product("Некорректный объект")
            self.assertIn("Можно добавлять только объекты класса Product или его наследников.", log.output[0])

    def test_products_property(self):
        self.category.add_product(self.product1)
        self.category.add_product(self.product2)
        expected_output = "Товар 1, 100 руб. Остаток: 10 шт.\nТовар 2, 200 руб. Остаток: 5 шт.\n"
        self.assertEqual(self.category.products, expected_output)

    def test_new_product_classmethod(self):
        product_data = {
            'name': 'Товар 3',
            'price': 300,
            'description': 'Описание товара 3',
            'quantity': 20
        }
        new_product = Category.new_product(product_data)
        self.assertEqual(new_product.name, 'Товар 3')
        self.assertEqual(new_product.price, 300)
        self.assertEqual(new_product.description, 'Описание товара 3')
        self.assertEqual(new_product.quantity, 20)

if __name__ == '__main__':
    unittest.main()

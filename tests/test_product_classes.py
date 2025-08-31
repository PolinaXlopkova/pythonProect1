import unittest
from src.product_classes import Smartphone, LawnGrass

class TestProductClasses(unittest.TestCase):

    def setUp(self):
        """Создание экземпляров классов перед каждым тестом."""
        self.smartphone1 = Smartphone("iPhone", 90, "14 Pro", 256, "black")
        self.smartphone2 = Smartphone("Samsung Galaxy", 85, "S21", 128, "blue")
        self.lawn_grass = LawnGrass("Kentucky Bluegrass", "USA", 14, "green")

    def test_smartphone_repr(self):
        """Тестирование метода __repr__ для класса Smartphone."""
        expected_repr = ("Smartphone(name=iPhone, efficiency=90, "
                         "model=14 Pro, memory=256, color=black)")
        self.assertEqual(repr(self.smartphone1), expected_repr)

    def test_lawn_grass_repr(self):
        """Тестирование метода __repr__ для класса LawnGrass."""
        expected_repr = ("LawnGrass(name=Kentucky Bluegrass, country=USA, "
                         "germination_period=14, color=green)")
        self.assertEqual(repr(self.lawn_grass), expected_repr)

    def test_add_smartphones(self):
        """Тестирование сложения двух объектов класса Smartphone."""
        result = self.smartphone1 + self.smartphone2
        expected_result = "Combined iPhone and Samsung Galaxy"
        self.assertEqual(result, expected_result)

    def test_add_lawn_grass(self):
        """Тестирование сложения двух объектов класса LawnGrass."""
        lawn_grass2 = LawnGrass("Perennial Ryegrass", "USA", 10, "dark green")
        result = self.lawn_grass + lawn_grass2
        expected_result = "Combined Kentucky Bluegrass and Perennial Ryegrass"
        self.assertEqual(result, expected_result)

    def test_add_different_types(self):
        """Тестирование сложения объектов разных типов (должно вызывать ошибку)."""
        with self.assertRaises(TypeError):
            _ = self.smartphone1 + self.lawn_grass

if __name__ == '__main__':
    unittest.main()

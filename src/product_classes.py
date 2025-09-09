class Product:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError(f"Cannot add {type(self).__name__} and {type(other).__name__}")
        return f"Combined {self.name} and {other.name}"


class Smartphone(Product):
    def __init__(self, name, efficiency, model, memory, color):
        super().__init__(name)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __repr__(self):
        return (f"Smartphone(name={self.name}, efficiency={self.efficiency}, "
                f"model={self.model}, memory={self.memory}, color={self.color})")


class LawnGrass(Product):
    def __init__(self, name, country, germination_period, color):
        super().__init__(name)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __repr__(self):
        return (f"LawnGrass(name={self.name}, country={self.country}, "
                f"germination_period={self.germination_period}, color={self.color})")

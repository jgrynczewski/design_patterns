class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


# Łamiemy OCP na przykładzie klasy ProductFilter
class ProductFilter:
    def filter_by_color(self, products, color):
        for product in products:
            if product.color==color:
                yield product

    def filter_by_size(self, products, size):
        for product in products:
            if product.size==size:
                yield product


# Klient
apple = Product('Apple', 'GREEN', "SMALL")
tree = Product('Tree', 'GREEN', "LARGE")
house = Product('House', "BLUE", "LARGE")

products = [ apple, tree, house ]

pf = ProductFilter()

print("Tylko zielone produkty:")
for item in pf.filter_by_color(products, "GREEN"):
    print(f"Produkt {item.name} jest zielony.")

print("Tylko duże produkty:")
for item in pf.filter_by_size(products, "LARGE"):
    print(f"Produkt {item.name} jest duży.")

print("######################################################")

# Interfejs specyfikacji
import abc
class ISpecification(abc.ABC):
    @abc.abstractmethod
    def is_satisfied(self, item):
        pass


# Nie łamimemy OCP (klasa Filter)
# wzorzec specyfikacja
class Filter:
    def filter(self, products, spec: ISpecification):
        for product in products:
            if spec.is_satisfied(product):
                yield product


class ColorSpecification(ISpecification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(ISpecification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


# Klient
new_pf = Filter()

green_specification = ColorSpecification("GREEN")
print("Tylko zielone produkty:")
for item in new_pf.filter(products, green_specification):
    print(f"Produkt {item.name} jest zielony.")

large_specification = SizeSpecification("LARGE")
print("Tylko duże produkty:")
for item in new_pf.filter(products, large_specification):
    print(f"Produkt {item.name} jest duży.")

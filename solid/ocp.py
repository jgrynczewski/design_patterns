# Open-Close Principle

class Animal:
    def __init__(self, name):
        self.name = name

# lista zwierząt
zoo = [
    Animal("Lion"),
    Animal("Mouse"),
    Animal("Snake"),
]

# Na przykładzie funkcji łamiemy OCP
def sound_animal(animals):
    for animal in animals:
        if animal.name == "Lion":
            print("RRrrrrr")
        elif animal.name == "Mouse":
            print("Pipipipi")
        elif animal.name == "Snake":
            print("SSSSSssss")


sound_animal(zoo)

print("#############################################################")

# Nie łamiemy OCP
class Animal():
    def make_sound(self):
        pass


class Lion(Animal):
    def make_sound(self):
        print("RRRRrrrr")


class Mouse(Animal):
    def make_sound(self):
        print("Pipipipi")


class Snake(Animal):
    def make_sound(self):
        print("SSSssss")


zoo = [
    Lion(),
    Mouse(),
    Snake()
]

def sound_animal(animals):
    for animal in animals:
        animal.make_sound()

sound_animal(zoo)

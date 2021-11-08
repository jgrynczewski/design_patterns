from farm import Cow
from farm import Horse
from farm import Animal

cow = Cow('Mućka', 2)
cow.say()
cow.feed()
cow.feed()
cow.give_milk()
cow.feed()

horse = Horse("Ben", 10)
horse.increase_age()
print(horse.age)


class Duck(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def say(self):
        print("Kwa kwa")


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)


duck = Duck("Daisy", 1)
duck.say()

dog = Dog("Azor", 2)
dog.say()


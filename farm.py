import abc

class Animal(abc.ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def increase_age(self):
        self.age += 1

    @abc.abstractmethod
    def say(self):
        pass


class Milk:
    def __init__(self, amount):
        self.__amount = amount

    def decrease_amount(self):
        self.amount -= 1


class Cow(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.is_hungry = True
        self.milk = Milk(3)

    def say(self):
        print("Muuu")

    def feed(self):
        if self.is_hungry:
            print("Karmimy")
            self.is_hungry = False
        else:
            print("Dziękuję, nie jestem głodna.")

    def give_milk(self):
        if self.is_hungry:
            print("Jestem głodna, więc nie dam mleka.")
            # self.milk.decrease_amount()
            self.decrease_milk()
        else:
            print("Daje mleka")
            self.is_hungry = True

    def decrease_milk(self):
        self.milk.amount -= 1


class Horse(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def say(self):
        print("Ihhahaha")

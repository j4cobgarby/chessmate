class Animal:
    def __init__(self, name):
        print("Animal  made")
        self.name = name

    def speak(self):
        print(self.name)

class Dog(Animal):
    def __init__(self, name, colour):
        super().__init__(name)
        self.colour = colour

    def speak(self):
        super().speak()
        print("bork")

class Cow(Animal):
    def __init__(self, name, milk_capacity):
        super().__init__(name)
        self.milk_capacity = milk_capacity

    def milk(self, amount):
        if self.milk_capacity - amount >= 0:
            self.milk_capacity -= amount
            print(f"Yay, you've taken {amount}ml milk from {self.name}. It now has {self.milk_capacity}ml left.")
        else:
            print("Sorry, there's not enough milk")

    def speak(self):
        print("*cow sound*")

myanimal = Animal("harry the human")
animal2 = Animal("arthur the aardvark")

d1 = Dog("rutherfordium", "beige")
d2 = Dog("chad", "duck egg green")

my_favourite_cow = Cow("Good Cow", 10000)
my_favourite_cow.milk(1540)

d1.speak()
d2.speak()
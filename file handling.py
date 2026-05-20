class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f'{self.name} makes a sound!')

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        print(f'{self.name} is {self.age}, is a {self.breed} and says Woof!')

class Cat(Animal):
    def speak(self):
        print(f'{self.name} is a {self.age} and says Meow!')

class Cow(Animal):
    def speak(self):
        print(f'{self.name} is {self.age} and says Moo!')

dog = Dog('Buddy', 6, "Labrador")
cat = Cat('Whiskers', 4)
cow = Cow("Brown", 3)
dog.speak()
cat.speak()
cow.speak()
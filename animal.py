
from abc import ABC,abstractmethod
from typing import Type

class Animal(ABC):
    def __init__(self,name:str):
        self.name = name

    @property
    @abstractmethod
    def isEdible(self)->bool:
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def quirk(self)->None:
        pass

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.name})"
        
    
class Cat(Animal):
    isEdible = False

    def move(self):
        pass

    def quirk(self):
        return "meow"

class Dog(Animal):
    isEdible = False
    
    def move(self):
        pass

    def quirk(self):
        return "bark"
    
class Chicken(Animal):
    isEdible = True
    
    def move(self):
        pass

    def quirk(self):
        return "tasty"

def print_animal_info(animal_class:Type[Animal],name:str):
    animal = animal_class(name)
    print(f"introduction: {animal}")
    print(f"{animal.__class__.__name__} do {animal.move.__name__}:{animal.move()}")
    print(f"{animal.__class__.__name__} do {animal.quirk.__name__}: {animal.quirk()}")
    print(f"Edible: {animal.isEdible}")

if __name__ == "__main__":
    print_animal_info(Cat,"wish")
    print_animal_info(Dog,"scooby")
    print_animal_info(Chicken,"chicken little")

        
    


from animal import Animal,Cat,Dog,Chicken
from typing import Dict,Union
import unittest

#UserDict Collection
class UserDictCollection:
    def __init__(self):
        self.animals: Dict[str,Animal] = {}

    def add(self,animal:Animal):
        self.animals[animal.name]=animal
        print("add")
        print(self.animals)

    def remove(self,name:str):
        if name in self.animals:
            del self.animals[name]
        print("remove")
        print(self.animals)
    
    def __getitem__(self,name:str) -> Union[Animal,None]:
        print("get")
        return self.animals.get(name)
    
    def __str__(self) -> str:
        print("str")
        return str(self.animals)
    
#unittest User Dictionary Collection
class TestUserDictCollection(unittest.TestCase):
    def setUp(self):
        self.animal_collection = UserDictCollection()
        self.cat = Cat("cio")
        self.dog = Dog("stuart")
        self.chicken = Chicken("star")
        self.animal_collection.add(self.cat)
        self.animal_collection.add(self.chicken)
        self.animal_collection.add(self.dog)

    def test_add_animals(self):
        expected_dict = {
            'cio': self.cat,
            'star':self.chicken,
            'stuart': self.dog,
        }
        actual_dict = self.animal_collection.animals
        self.assertEqual(expected_dict,actual_dict)

    def test_remove_animals(self):
        self.animal_collection.remove("star")
        expected_dict = {
            'cio': self.cat,
            'stuart': self.dog,
        }
        actual_dict = self.animal_collection.animals
        self.assertEqual(expected_dict,actual_dict)

    def test_get_animals(self):
        get_animal = self.animal_collection["cio"]
        self.assertEqual(get_animal,self.cat)

    def test_get_animals_nonexists(self):
        get_animal = self.animal_collection["appa"]
        self.assertIsNone(get_animal)
         
if __name__ == "__main__":
    unittest.main()
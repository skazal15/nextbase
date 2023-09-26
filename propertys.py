class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero.")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        celsius_equivalent = (value - 32) * 5/9
        print("setter")
        self.celsius = celsius_equivalent

# Kode utama
temp = Temperature(25)

print("Celsius:", temp.celsius)
print("Fahrenheit:", temp.fahrenheit)

temp.celsius = 0
print("Updated Celsius:", temp.celsius)
print("Updated Fahrenheit:", temp.fahrenheit)

temp.fahrenheit = -400
print("Updated Celsius from Fahrenheit:", temp.celsius)
print("Updated Fahrenheit:", temp.fahrenheit)

import time

def timeme(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper

@timeme
def slow_function():
    i=[1,2,3,4]
    x = [a for a in i if a%2 != 0]
    print(x)
    print("Function executed")

slow_function()

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._width * self._height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            print("Width must be a positive value")

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            print("Height must be a positive value")

rect = Rectangle(5, 3)
rect.width = -2    # Output: Width must be a positive value
print(rect.area)   # Output: 15


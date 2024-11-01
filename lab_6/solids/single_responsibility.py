""" 
single_responsibility.
each class should have at most one responsibility
"""
from math import pi

class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return pi * (self.radius ** 2)

class Triangle:
    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height

    def area(self) -> float:
        return 0.5 * self.base * self.height

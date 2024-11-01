"""
interface_segregation
classes should not be forced to 
implement the interfaces they don't use
"""
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

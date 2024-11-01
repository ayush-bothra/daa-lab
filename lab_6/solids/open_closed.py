"""
open_closed
each class should be open for extension 
and closed for modification
"""
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

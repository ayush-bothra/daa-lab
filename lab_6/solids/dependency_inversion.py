"""
dependency_inversion
high level modules should not depend on 
the low_level modules but rather on abstractions 
"""
from open_closed import Shape

class AreaCalculator:
    def calculate_area(self, shape: Shape) -> float:
        return shape.area()

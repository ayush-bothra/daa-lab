# main.py
from liskov_substitution import Rectangle, Circle, Triangle
from dependency_inversion import AreaCalculator

def main():
    shapes = [Rectangle(3, 4), Circle(5), Triangle(6, 7)]
    calculator = AreaCalculator()

    for shape in shapes:
        print(f"Area: {calculator.calculate_area(shape):.2f}")

if __name__ == "__main__":
    main()

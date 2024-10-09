"""
Author: Ayush Bothra
Date: 03-10-2024
Aim: Implement fast multiplication using Karatsuba's algorithm
     and understand its divide and conquer aspects.
"""
import math

import math

class FastMultiplier:
    """
    Computes the multiplication of two numbers using Karatsuba's algorithm.
    
    Methods:
    - karatsuba(num1, num2): Returns the product of num1 and num2.
    """
    def check_for_errors(self, num1, num2):
        # Check if inputs are floats or not integers
        if not isinstance(num1, int) or not isinstance(num2, int):
            return -1 

    def karatsuba(self, num1, num2):
        """Performs multiplication using Karatsuba's algorithm with log properties."""
        
        # Handle sign only at the top level
        sign = -1 if (num1 < 0) ^ (num2 < 0) else 1
        num1, num2 = abs(num1), abs(num2)

        # Base case: when numbers are small enough, perform direct multiplication
        if num1 < 10 or num2 < 10:
            return sign * (num1 * num2)

        # Calculate the number of digits using the logarithmic approach
        m = max(math.floor(math.log10(num1) + 1), math.floor(math.log10(num2) + 1)) // 2  

        # Split the numbers into high and low parts using divmod
        high1, low1 = divmod(num1, 10**m)
        high2, low2 = divmod(num2, 10**m)

        z0 = self.karatsuba(low1, low2)
        z1 = self.karatsuba(low1 + high1, low2 + high2)
        z2 = self.karatsuba(high1, high2)

        result = (z2 * (10**(2 * m))) + ((z1 - z2 - z0) * (10**m)) + z0

        return sign * result 



if __name__ == '__main__':
    test_cases = [
        (12, 34),
        (56, 56),
        (90, 23),
        (12.34, 56.78),
        (90.12, 34.56),
        (7.89, 1.23),
        ("abc", 45.67),
        (-1234567890, 9876543210),
        (1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890, 
        9876543210987654321098765432109876543210987654321098765432109876543210987654321098765432109876543210),
        (5, 3),
    ]
    
    for test_case in test_cases:
        multiplier = FastMultiplier()
        error = multiplier.check_for_errors(test_case[0], test_case[1])
        if error == -1:
            print(f"Error: Invalid input for {test_case[0]} and {test_case[1]}. One or both inputs are not integers.")
        else:
            result = multiplier.karatsuba(test_case[0], test_case[1])
            print(f"Multiplication result of {test_case[0]} and {test_case[1]}: {result}")

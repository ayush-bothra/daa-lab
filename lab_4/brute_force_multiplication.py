"""
Author: Ayush Bothra
Aim: Implement the grade-school method of multiplication
"""

class Multiply():
    """
    This is a class to store the functions that multiply two 
    large numbers using grade-school multiplication.

    Attributes: 
    num1: first number in integer form
    num2: second number in integer form
    result array: returning the product

    methods: 
    init(self, num1, num2) -> result size array and the two numbers 
    brute_force_multiply(None) -> the multiplication of the numbers 
                                  as an integer
    """

    def __init__(self, num1, num2):
        # Initialize attributes
        self.result = [0] * (len(str(abs(num1))) + len(str(abs(num2))))  # Calculate the result size based on absolute values
        self.num1 = abs(num1)
        self.num2 = abs(num2)
        self.negative = (num1 < 0) ^ (num2 < 0)  # Set negative to True if one is negative

    def handle_carry(self, i, j):
        # Handle carry if any
        if self.result[i + j] >= 10:
            self.result[i + j + 1] += self.result[i + j] // 10
            self.result[i + j] %= 10

    def return_output(self):
        # Reverse the result and convert it back to a single number
        self.result = self.result[::-1]
        
        # Remove leading zeros
        while len(self.result) > 1 and self.result[0] == 0:
            self.result.pop(0)

        # Convert to string and handle sign
        result = int(''.join(map(str, self.result)))
        return result * -1 if self.negative else result

    def check_for_errors(self):
        # Check if inputs are floats or not integers
        if not isinstance(self.num1, int) or not isinstance(self.num2, int):
            return -1 

    def brute_force_multiply(self):
        str_num1 = str(self.num1)[::-1]  # Convert to string for manipulation
        str_num2 = str(self.num2)[::-1]

        for i in range(len(str_num1)):
            for j in range(len(str_num2)):
                _digit_product = int(str_num1[i]) * int(str_num2[j])
                
                # Add to result array at appropriate position (i+j for positional shift)
                self.result[i + j] += _digit_product
                self.handle_carry(i, j)

        return self.return_output()


if __name__ == "__main__":
    test_cases = [
        (12,34),
        (56, 56),
        (90, 23),
        (12.34, 56.78),
        (90.12, 34.56),
        (7.89, 1.23),
        ("abc", 45.67),
        (-1234567890, 9876543210),
        (1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890, 
        9876543210987654321098765432109876543210987654321098765432109876543210987654321098765432109876543210),
        (5, 3)
    ]

    for test_case in test_cases:
        if type(test_case[0]) == str or type(test_case[1]) == str:
            print(f"{test_case} has the wrong type")
            continue
        operator = Multiply(test_case[0], test_case[1])

        # Check for errors before multiplying
        if operator.check_for_errors() == -1:
            print("Error: One or both inputs are float values.")
        else:
            result = operator.brute_force_multiply()
            print(f"result: {result}")

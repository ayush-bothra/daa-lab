
# imports
import math
from math import ceil, log2

class ProcessFile:
    def __init__(self):
        pass

    def take_file(self, file_path):
        with open(file_path, 'r') as file:
            reader = file.read()
        return reader


class Encode:
    """
    the method for fixed size is:
    1. find the total number of unique variables
    (an easy way is to convert the whole document
    into a set and then find the size of the set)
    2. check which power of two is the nearest to that
    amount
    3. then whatever power is obtained, that will be 
    the size of each variable
    4. sort the set/ if sorted dont do this step
    5. start from the start and assign a binary
    code to each value
    6. finally create a new text using this mapping
    this will be the encoding
    """
    def __init__(self):  # Add 'self' parameter
        pass

    def convert_to_binary(self, number):
        if number == 0:
            return '0'
        if number == 1:
            return '1'
        return self.convert_to_binary(number // 2) + str(number % 2)

    def encode(self, file_string):
        unique_variables = set(file_string)
        number_of_unique_variables = len(unique_variables)

        if number_of_unique_variables == 0:
            return {}  # Handle empty case

        fixed_size = ceil(log2(number_of_unique_variables))

        unique_variables = sorted(unique_variables)  # Sort the unique characters
        encoder = {}

        frequency = {}
        for char in file_string:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
        for i in range(number_of_unique_variables):
            # Create zero-padded binary representation
            binary_representation = self.convert_to_binary(i).zfill(fixed_size)
            encoder[unique_variables[i]] = binary_representation

        original_size = len(file_string) * 8 # ascii value
        encoded_size = sum(frequency[char] * fixed_size for char in unique_variables)
        return encoder, original_size, encoded_size  # Return the encoding mapping

# Example usage
file_processor = ProcessFile()
file_content = file_processor.take_file('lab_5/huffman_text/case_5.txt')  # Provide the correct file path
encoder = Encode()
encoding_map, original_size, encoded_size = encoder.encode(file_content)

print(encoding_map)  # This will print the character to binary mapping
print(original_size)
print(encoded_size)
print(f"{encoded_size / original_size:.2f}")

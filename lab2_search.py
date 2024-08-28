""" 
Name: Ayush Bothra
Roll No: 231070011
Date: 10-08-2024
Algorithm: Linear and Binary Search
"""


def linear_search(a, target):
    """Function to search an array by linear search."""
    for idx, value in enumerate(a):
        if value == target:
            return idx
    return "not found"


def sorted(array):
    for i in range(len(array)-1):
        # Checking if the array is sorted
        if array[i] > array[i + 1]:
            return False
    return True
        

def binary_search(a, target, left, right):
    """Recursive function to search an array by binary search."""
    if left > right:
        return "not found"
    
    middle = left + (right - left) // 2
    if a[middle] == target:
        return middle
    if a[middle] < target:
        return binary_search(a, target, middle + 1, right)
    if a[middle] > target:
        return binary_search(a, target, left, middle - 1)


if __name__ == "__main__":
    # using a dictionary to store multiple test-cases.
    # the key is target, the value is the array.
    linear_tests = {
        8: [3, 7, 4, 1, 2, 6],
        9: [],
        12: [-12, 13, 8, 16, 12],
        200: [7, -30, -100, 200, 8],
        -1: [2, 7, 9, -10, -1, -3],
        }

    binary_tests = {
        3: [3, 6, 7, 2, 1, -1],
        8: [-1, 1, 2, 4, 8],
        -2: [-1, 2, 3, 6, 8, 10],
        4: [-10, -5, 4, 7],
        9: [2, 7, 9, 11, 13],
        }

    print("output for linear search:")
    for key  in linear_tests.keys():
        print(f"array: {linear_tests[key]}, target: {key}")
        print(f"element position: {linear_search(linear_tests[key],key)}")

    print("# ------------------------------------------------ #")
    print("output for binary search: ")
    for key in binary_tests.keys():
        print(f"array: {binary_tests[key]}, target: {key}")
        if sorted(binary_tests[key]):
            position = binary_search(binary_tests[key],key,
                                     0,len(binary_tests[key]))
            print(f"element position: {position}")    
        else:
            print("element position: not found")
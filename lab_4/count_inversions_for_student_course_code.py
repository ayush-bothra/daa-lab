"""
Author: Ayush Bothra
Aim: To implement the algorithm for count inversions
     using student course codes as the array element
"""
import os
import pandas as pd
from collections import defaultdict


class Course_code_ranker():
    """
    This class provides functionality to count the number of inversions 
    in arrays of student course codes, comparing student course rankings 
    against a predefined base order. It uses the divide-and-conquer 
    approach (merge sort) to efficiently count inversions.

    Attributes:
        base_array_order (list): A predefined list representing the standard course order.
        inversion_counts (defaultdict): A dictionary to store the frequency of 
                                        inversion counts for student course lists.
    
    Methods:
        count_inversions(array): Recursively counts the number of inversions in an array.
        find_split_inversions(array1, array2): Merges two sorted arrays while counting split inversions.
        compare_student_course_lists(student_courses): Compares a list of student course lists 
                                                       and counts inversions for each.
        return_results(): Returns the inversion counts as a dictionary.
    """

    def __init__(self): 
        self.base_course_order = [101, 102, 103, 104, 105, 106, 107, 108]
        self.inversion_counts = defaultdict(int)

    def count_inversions(self, array):
        if len(array) <= 1:
            return 0, array
    
        mid = len(array)//2
        left_inv, left = self.count_inversions(array[:mid])
        right_inv, right = self.count_inversions(array[mid:])
        int_inv, int_array = self.find_split_inversions(left, right)
        total_inversions = left_inv + int_inv + right_inv
        return total_inversions, int_array

    def find_split_inversions(self, array1, array2):
        merged = []
        i = 0
        j = 0
        count = 0

        while i < len(array1) and j < len(array2):
            if array1[i] <= array2[j]:
                merged.append(array1[i])
                i += 1
            else:
                merged.append(array2[j])
                count += len(array1) - i
                j += 1

        while i < len(array1):
            merged.append(array1[i])
            i += 1

        while j < len(array2):
            merged.append(array2[j])
            j += 1

        return count, merged
    
    def compare_student_course_lists(self, student_courses):
        if not any(x not in self.base_course_order for student_course in student_courses for x in student_course):    
            for student_course in student_courses: 
                inversion_count, _ = self.count_inversions(student_course)
                self.inversion_counts[inversion_count] += 1

    def return_results(self):
        if not self.inversion_counts:
            return -1
        return self.inversion_counts


if __name__ == "__main__":

    for file_num in range(1,11):
        compare_course_rank = Course_code_ranker()
        file_path = f"students_courses_{file_num}.csv"

        try:
            student_course_df = pd.read_csv(file_path)
        except Exception as e:
            print(f"An unexpected error occurred while reading {file_path}: {e}")
            print("###########################################################")
            continue

        # checking if the cells are empty
        if pd.isna(student_course_df).any().any() or (student_course_df == '').any().any():
            print(f"the {file_path} has empty cells")
            print("###########################################################")
            continue

        # create a list of the courses, barring the student ID column
        student_course_list = student_course_df.iloc[:,1:].values.tolist()
        if len(student_course_list) == 0:
            print(f"Student_course_{file_num} is empty")
            print("###########################################################")
            continue

        compare_course_rank.compare_student_course_lists(student_course_list)
        output = compare_course_rank.return_results()
        
        if output == -1:
            print(f"{file_path} has invalid course codes")
            print("###########################################################")
            continue

        total = 0
        for key, value in sorted(output.items()): # first sorts, then iterates so still nlogn
            if key < 4:
                print(f"{key} inversions occured for {value} students in the given array")
            else:
                total += value
        print(f"more than 3 inversions were found in {total} students")
        print("###########################################################")

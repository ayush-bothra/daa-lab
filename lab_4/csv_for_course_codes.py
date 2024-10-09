import random
import csv

# Base course order
base_course_order = [101, 102, 103, 104, 105, 106, 107, 108]

def generate_course_list_with_inversions(base_list, max_inversions):
    """
    Generate a course list with a specific number of inversions
    by swapping elements in the list.
    """
    course_list = base_list.copy()
    
    # Perform a random number of swaps (between 0 and max_inversions)
    num_swaps = random.randint(0, max_inversions)
    
    for _ in range(num_swaps):
        i, j = random.sample(range(len(course_list)), 2)  # Pick two distinct indices
        course_list[i], course_list[j] = course_list[j], course_list[i]  # Swap elements
    
    return course_list

# Loop to generate 10 CSV files
for file_num in range(1, 11):
    file_name = f'students_courses_{file_num}.csv'
    
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header
        writer.writerow(['Student_ID', 'Course_1', 'Course_2', 'Course_3', 'Course_4', 
                         'Course_5', 'Course_6', 'Course_7', 'Course_8'])
        
        # Generate CSV file with 100 students
        for student_id in range(1, 101):
            # Generate a course list with 0-3 inversions
            student_courses = generate_course_list_with_inversions(base_course_order, max_inversions=3)
            
            # Write the student's ID and course list to the CSV
            writer.writerow([f'Student_{student_id}'] + student_courses)

    print(f"CSV file '{file_name}' generated with course lists containing up to 3 inversions.")

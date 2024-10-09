def bubble_sort_with_inversion_count(array):
    count = 0
    n = len(array)

    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                # Count the inversion
                count += 1
                # Swap the elements
                array[j], array[j + 1] = array[j + 1], array[j]

    return count, array

if __name__ == '__main__':
    array = [4, 7, 3, 9, 10, 4, 5]
    count_inversions, sorted_array = bubble_sort_with_inversion_count(array)
    print(f'Sorted Array: {sorted_array}, Inversion Count: {count_inversions}')

def bubblesort(array):
    n = len(array)

    # Traverse through all array elements
    for i in range(n - 1):
        # Last i elements are already sorted, so we don't need to check them
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array

# Example usage with three arrays
array1 = [64, 34, 25, 12, 22, 11, 90]
sorted_array1 = bubblesort(array1)
print("Original Array 1:", array1)
print("Sorted Array 1:", sorted_array1)

"""

Sorts a list using the insertion sort algorithm

Input: A list of integers
Output: A list containing the same integers as the input, but sorted in ascending order

For each element in the unsorted list, swap with the previous element until it is correctly placed in the sorted list
"""


def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        while i > 0 and arr[i-1] > temp:
            arr[i] = arr[i - 1]
            i = i-1
        arr[i] = temp
    return arr

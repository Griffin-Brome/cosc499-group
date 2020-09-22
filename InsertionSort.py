"""
Sorts integers using insertion sort

Takes an array of integers as input
"""


def insertionSort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        while i > 0 and arr[i-1] > temp:
            arr[i] = arr[i - 1]
            i = i-1
        arr[i] = temp
    return arr

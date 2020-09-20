""""
Pytest tests for insertion sort from InsertionSort.py
"""
from InsertionSort import *


def test_insertion_sort():
    unsorted_arr = [1, 5, 7, 3, 2]
    insertionSort(unsorted_arr)
    assert unsorted_arr == [1, 2, 3, 5, 7]

if __name__ == "__main__":
    test_insertion_sort()

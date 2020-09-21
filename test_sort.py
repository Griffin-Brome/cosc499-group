""""
Pytest tests for insertion sort from InsertionSort.py
"""
from InsertionSort import *


def test_insertion_sort():
    unsorted_arr = [1, 5, 7, 3, 2]
    insertion_sort(unsorted_arr)
    assert unsorted_arr == [1, 2, 3, 5, 4]

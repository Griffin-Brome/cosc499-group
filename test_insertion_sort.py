from insertion_sort import *


def test_insertion_sort():
    unsorted_arr = [1, 5, 7, 3, 2]
    assert insertion_sort(unsorted_arr) == [1, 2, 3, 5, 7]


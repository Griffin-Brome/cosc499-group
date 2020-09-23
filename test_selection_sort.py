from selection_sort import *


def test_selection_sort():
    unsorted_list = [9, 4, 5, 1, 2, 13, 28, 31]
    sorted_list = [1, 2, 4, 5, 9, 13, 28, 31]
    assert selection_sort(unsorted_list) == sorted_list

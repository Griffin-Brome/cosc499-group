"""
Pytest tests for bubble sort from bubble_sort.py
"""
import unittest
from bubble_sort import bubble_sort


def test_bubble_sort():
	x=[9,8,7,6,5,4,3,2,1]
	
	assert(bubble_sort(x)==[1,2,3,4,5,6,7,8,9])
	print("Test Complete")

test_bubble_sort()

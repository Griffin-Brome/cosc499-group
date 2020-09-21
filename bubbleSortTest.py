import unittest
from bubbleSort import bubbleSort


def test_bubble_sort():
	x=[9,8,7,6,5,4,3,2,1]
	#print(bubbleSort(x))
	assert(bubbleSort(x)==[1,2,3,4,5,6,7,8,9])

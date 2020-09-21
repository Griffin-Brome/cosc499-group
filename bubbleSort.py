"""Return a sorted Array

Takes an array
"""

def bubbleSort(array):
    for z in range(len(array)-1):
        for x in range(len(array)-1):
            for y in range(len(array)-1):
                if(array[x]>array[x+1]):
                    temp = array[x]
                    array[x] = array[x+1]
                    array[x+1] = temp

    return array
        

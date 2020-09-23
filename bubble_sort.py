

def bubble_sort(array):
    """
    Sorts a list using bubble sort algorithm

    Input: A list of integers
    Output: A list containing the same integers as the input, but sorted in
            ascending order

    Sorts by iterating through a list swapping values that are in the wrong order.
    Stops when it is impossible for unsorted elements to remain.
    """
    for z in range(len(array)-1):
        for x in range(len(array)-1):
            for y in range(len(array)-1):
                if(array[x]>array[x+1]):
                    temp = array[x]
                    array[x] = array[x+1]
                    array[x+1] = temp

    return array
        

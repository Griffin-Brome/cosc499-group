def selection_sort(input):
    """
    Sorts a list using the selection sort algorithm

    Input: A list of integers
    Output: A list containing the same integers as the input, but sorted in
            ascending order

    For each element in the unsorted list, find the smallest element after it,
    then swap the two
    """

    for i,val in enumerate(input):
        min_val = val
        min_idx = i

        for k in input[i+1:]:
            if k < min_val:
                min_val = k
                min_idx = input.index(k)
        input[i], input[min_idx] = input[min_idx], input[i]
    return input

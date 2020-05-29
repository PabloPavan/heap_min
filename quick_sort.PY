"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

def partition(array, start,end):
    pivot = array[end]
    i = start
    for j in range(start, end):
        if(array[j] <= pivot):
            array[j], array[i] = array[i], array[j]
            i+=1
    array[i], array[end] = array[end], array[i]
    return i

def q_sort(array, start=0, end = None):
    if end is None:
        end = len(array)-1
    if start < end:
        pivot = partition(array, start, end)
        q_sort(array, start, pivot-1)
        q_sort(array, pivot+1, end)
    return array
        

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print q_sort(test)

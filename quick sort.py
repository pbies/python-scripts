#!/usr/bin/env python3

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Example usage:
my_list = [5, 2, 9, 1, 7, 6, 3]
sorted_list = quick_sort(my_list)
print(sorted_list)

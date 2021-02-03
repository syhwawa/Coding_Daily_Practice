#https://medium.com/@george.seif94/a-tour-of-the-top-5-sorting-algorithms-with-python-code-43ea9aa02889
#Bubble Sort
"""
Bubble sort steps through the list and compares adjacent pairs of elements,The elements are swapped if they are in the wrong order. The pass through the unsorted portion of the list is repeated until the list is sorted. 
Because Bubble sort repeatedly passes through the unsorted part of the list, it has a worst case complexity of O(n²).
"""

def bubble_sort(array):
    def swap(first_element, second_element):#Swap the element
        array[first_element], array[second_element] = array[second_element], array[first_element]
        
    length = len(array)
    
    for i in range(length):
        j = 0
        stop = length - i # Only nned to check n-i element
        while j < stop - 1:
            if array[j] > array[j + 1]:
                swap(j, j + 1)
            j += 1
    
    return array
    
# TC: O(n²)
# SC: O(1)

print(bubble_sort([3,2,5,1]))
def bubble_sort(our_list):
    # We go through the list as many times as there are elements
    for i in range(len(our_list)):
        # We want the last pair of adjacent elements to be (n-2, n-1)
        for j in range(len(our_list) - 1):
            if our_list[j] > our_list[j+1]:
                # Swap
                our_list[j], our_list[j+1] = our_list[j+1], our_list[j]
                
#Optimization
"""
1. When no swaps are made, that means that the list is sorted. Though, with the previously implemented algorithm, it'll keep evaluating the rest of the list even though it really doesn't need to. 
To fix this, we'll keep a boolean flag and check if any swaps were made in the previous iteration
"""

def bubble_sort(our_list):
    # We want to stop passing through the list
    # as soon as we pass through without swapping any elements
    has_swapped = True

    while(has_swapped):
        has_swapped = False
        for i in range(len(our_list) - 1):
            if our_list[i] > our_list[i+1]:
                # Swap
                our_list[i], our_list[i+1] = our_list[i+1], our_list[i]
                has_swapped = True
"""
2. The first time we pass through the list the position n is guaranteed to be the largest element, 
the second time we pass through the position n-1 is guaranteed to be the second-largest element and so forth.
"""

def bubble_sort(our_list):
    has_swapped = True

    num_of_iterations = 0

    while(has_swapped):
        has_swapped = False
        for i in range(len(our_list) - num_of_iterations - 1):
            if our_list[i] > our_list[i+1]:
                # Swap
                our_list[i], our_list[i+1] = our_list[i+1], our_list[i]
                has_swapped = True
        num_of_iterations += 1

Given an array of integers, print the array in such a way that the first element is first maximum and second element is first minimum and so on.

Examples :

Input : arr[] = {7, 1, 2, 3, 4, 5, 6}
Output : 7 1 6 2 5 3 4

Input : arr[] = {1, 6, 9, 4, 3, 7, 8, 2}
Output : 9 1 8 2 7 3 6 4

```Python
def alternateSort(arr, n): 
  
    # Sorting the array 
    arr.sort()  
  
    # Printing the last element of array  
    # first and then first element and then  
    # second last element and then second  
    # element and so on. 
    i = 0
    j = n-1
    res = []
    while (i < j):  
      
        res.append(arr[j])
        res.append(arr[i])
        j-= 1
        i+= 1
    # If the total element in array is odd  
    # then print the last middle element. 
    if (n % 2 != 0): 
        res.append(arr[i])
    return res
  
# Driver code 
arr = [-1,1,2,3,-5]  
n = len(arr) 
  
alternateSort(arr, n)  
```

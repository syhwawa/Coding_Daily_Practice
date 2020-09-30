Fix the bug in one line of code, fix it. 

Example a = [2, 4, 6, 8, 10], k = 3, the output should be [[8, 10], [2, 10], [2, 4]]
becasue you can remove, [2, 4, 6], [4, 6, 8], [6, 8, 10]

```Python
def removekelements(a, k):
    n = len(a)
    result = lambda arr, idx: arr[0:(idx)] +arr[(idx+k):n]
    return [result(a, i) for i in range(n - k + 1)]

a = [2, 4, 6, 8, 10, 12]
k = 3
removekelements(a, k)
```

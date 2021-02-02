# Ocado Coding interview
# Solution 1: Iteratively
def fibonacci_series_num(n):
    a = 0
    b = 1
    for i in range(n):
        c = a + b
        a = b 
        b = c
    return b
for i in range(10):
    print(fibonacci_series_num(i))
# TC:O(N), SC:O(N)

def fibonacci_series_num(n):
    if n <= 1:
        return n
    else:
        return fibonacci_series_num(n-1) + fibonacci_series_num(n-2)

for i in range(1, 10):
    print(fibonacci_series_num(i))
    
# Time complexity: our solution O(2**n) is an upper bound for the time complexity of F(n).
# Space Complexity: For Fibonacci recursive implementation or any recursive algorithm, 
# the space required is proportional to the maximum depth of the recursion tree
# https://medium.com/@syedtousifahmed/fibonacci-iterative-vs-recursive-5182d7783055

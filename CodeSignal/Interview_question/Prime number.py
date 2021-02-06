# Feature Space Coding
"""Given a number n, how to determine if it is prime number."""


# Python program to display all the prime numbers within an interval

lower = 900
upper = 1000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

# Follow up: Do it in more efficient way

# Python Program to find prime numbers in a range 
import time 
def is_prime(n): 
    if n <= 1: 
        return False
    for i in range(2,n): 
        if n % i == 0: 
            return False
    return True
  
# Driver function 
t0 = time.time() 
c = 0 #for counting 
  
for n in range(1,100000): 
    x = is_prime(n) 
    c += x 
print("Total prime numbers in range :", c) 
  
t1 = time.time() 
print("Time required :", t1 - t0) 

Method 2
In this method, we use a simple trick by reducing the number of divisors we check for. We have found that there is a fine line which acts as the mirror as shows the factorization below the line and factorization above the line just in reverse order. The line which divided the factors into two halves is the line of the square root of the number. If the number is a perfect square, we can shift the line by 1 and if we can get the integer value of the line which divides.

36=1*36          
  =2*18
  =3*12
  =4*9
------------
  =6*6
------------
  =9*4
  =12*3
  =18*2
  =36*1
In this function, we calculate an integer, say max_div, which is the square root of the number and get its floor value using the math library of Python. In the last example, we iterate from 2 to n-1. But in this, we reduce the divisors by half as shown. You need to import the math module to get the floor and sqrt function.
Following are the steps used in this method:

If the integer is less than equal to 1, it returns False.
Now, we reduce the numbers which needs to be checked to the square root of the given number.
If the given number is divisible by any of the numbers from 2 to the square root of the number, the function will return False
Else it will return True
filter_none
edit
play_arrow

brightness_4
# Python Program to find prime numbers in a range 
import math 
import time 
def is_prime(n): 
    if n <= 1: 
        return False
  
    max_div = math.floor(math.sqrt(n)) 
    for i in range(2, 1 + max_div): 
        if n % i == 0: 
            return False
    return True
  
# Driver function 
t0 = time.time() 
c = 0 #for counting 
  
for n in range(1,100000): 
    x = is_prime(n) 
    c += x 
print("Total prime numbers in range :", c) 
  
t1 = time.time() 
print("Time required :", t1 - t0)


Method 3
Now, we will optimize our code to next level which takes lesser time than the previous method. You might have noticed that in the last example, we iterated through every even number up to the limit which was a waste. The thing to notice is that all the even numbers except two can not be prime number. In this method, we kick out all the even numbers to optimize our code and will check only the odd divisors.
Following are the steps used in this method:

If the integer is less than equal to 1, it returns False.
If the number is equal to 2, it will return True.
If the number is greater than 2 and divisible by 2, then it will return False.
Now, we have checked all the even numbers. Now, look for the odd numbers.
If the given number is divisible by any of the numbers from 3 to the square root of the number skipping all the even numbers, the function will return False
Else it will return True
filter_none
edit
play_arrow

brightness_4
# Python Program to find prime numbers in a range 
import math 
import time 
def is_prime(n): 
    if n <= 1: 
        return False
    if n == 2: 
        return True
    if n > 2 and n % 2 == 0: 
        return False
  
    max_div = math.floor(math.sqrt(n)) 
    for i in range(3, 1 + max_div, 2): 
        if n % i == 0: 
            return False
    return True
  
# Driver function 
t0 = time.time() 
c = 0 #for counting 
  
for n in range(1,100000): 
    x = is_prime(n) 
    c += x 
print("Total prime numbers in range :", c) 
  
t1 = time.time() 
print("Time required :", t1 - t0) 
Output:

Total prime numbers in range: 9592
Time required: 0.23305177688598633
In the above code, we check all the numbers from 1 to 100000 whether those numbers are prime or not. It takes comparatively lesser time than all the previous methods for running the program. It is most efficient and quickest way to check for the prime number. Therefore, it is most preferred in competitive programming. Next time while attempting any question in competitive programming, use this method for best results.

https://www.geeksforgeeks.org/analysis-different-methods-find-prime-number-python/

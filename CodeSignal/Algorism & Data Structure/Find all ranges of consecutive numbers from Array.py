# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 15:13:59 2020

@author: syhwawa
"""

"""
Given a sorted array arr[] consisting of N integers without any duplicates, the task is to find the ranges of consecutive numbers from that array.
Examples:

Input: arr[] = {1, 2, 3, 6, 7} 
Output: 1->3, 6->7 
Explanation: 
There are two ranges of consecutive number from that array. 
Range 1 = 1 -> 3 
Range 2 = 6 -> 7
Input: arr[] = {-1, 0, 1, 2, 5, 6, 8} 
Output: -1->2, 5->6, 8 
Explanation: 
There are three ranges of consecutive number from that array. 
Range 1 = -1 -> 2 
Range 2 = 5 -> 6 
Range 3 = 8

https://www.geeksforgeeks.org/find-all-ranges-of-consecutive-numbers-from-array/
"""

a = [0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]
res = []
length = 1
for i in range(1, len(a) + 1):
    if (i == len(a) or (a[i] - a[i-1] ) != 1):
        if length == 1:
            res.append(str(a[i-length]))
        else:
            res.append(str(a[i-length]) + '->' + str(a[i - 1]))
        lenght = 1
    else:
        length += 1

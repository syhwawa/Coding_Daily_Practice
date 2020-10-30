# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 15:58:46 2020

@author: syhwawa
"""

"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

"""
def productExceptSelf(nums):
    res = [1 for _ in nums]
    
    left = 1
    right = 1
    
    for i in range(len(nums)):
        res[i] *= left
        res[-1-i] *= right
        left *=nums[i]
        right *= nums[-1-i]
        
    return res

nums = [1,2,3,4]
productExceptSelf(nums)

def productExceptSelf(nums):
    res = [1 for _ in nums]
    
    left = 1
    right = 1
    
    for i in range(len(nums)):
        res[i] *= left
        res[-1-i] *= right
        left *=nums[i]
        right *= nums[-1-i]
        
    return res

nums = [1,2,3,4]
productExceptSelf(nums)
        

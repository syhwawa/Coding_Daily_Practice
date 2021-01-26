# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 00:20:15 2020

@author: syhwawa
We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’. The array originally contained all the numbers from 1 to ‘n’, but due to a data error, one of the numbers got duplicated which also resulted in one number going missing. Find both these numbers.

Example 1:

Input: [3, 1, 2, 5, 2]
Output: [2, 4]
Explanation: '2' is duplicated and '4' is missing.
Example 2:

Input: [3, 1, 2, 3, 6, 4]
Output: [3, 5]
Explanation: '3' is duplicated and '5' is missing.
"""
def find_corrupt_numbers(nums):
  # TODO: Write your code here
  i = 0
  while i < len(nums):
    j = nums[i] - 1
    if nums[i] != nums[j]:
        nums[i], nums[j] = nums[j], nums[i]  # swap
    else:
      i += 1
  res = []
  for i in range(len(nums)):
    if nums[i] != i + 1:
      res.append(nums[i])
      res.append(i + 1)
 
  return res


#Time complexity #
#The time complexity of the above algorithm is O(n)O(n).

#Space complexity #
# algorithm runs in constant space O(1)O(1).

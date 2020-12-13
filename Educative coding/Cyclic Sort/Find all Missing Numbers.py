# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 21:02:14 2020
We are given an unsorted array containing numbers taken from the range 1 to ‘n’. The array can have duplicates, which means some numbers will be missing. Find all those missing numbers.

Example 1:

Input: [2, 3, 1, 8, 2, 3, 5, 1]
Output: 4, 6, 7
Explanation: The array should have all numbers from 1 to 8, due to duplicates 4, 6, and 7 are missing.
Example 2:

Input: [2, 4, 1, 2]
Output: 3
Example 3:

Input: [2, 3, 2, 1]
Output: 4

@author: syhwawa
"""
def find_missing_numbers(nums):
  i, n = 0, len(nums)
  res = []
  while i < n:
    j = nums[i] - 1
    if nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]  # swap
    else:
      i += 1

  for i in range(n):
    if nums[i] != i + 1:
      res.append(i + 1)

  return res
#Time complexity #
#The time complexity of the above algorithm is O(n).

#Space complexity #
#Ignoring the space required for the output array, the algorithm runs in constant space O(1).

#Solution 2 Hashset

def find_missing_numbers(nums):
  dic = set()
  res = []
  for i in nums:
    dic.add(i)
  for i in range(1, len(nums)+1):
    if i not in dic:
      res.append(i)

  return res
# TC: O(N)
# SC: O(N)

# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 20:55:51 2020

@author: syhwawa
We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’. The array has some numbers appearing twice, find all these duplicate numbers without using any extra space.

Example 1:

Input: [3, 4, 4, 5, 5]
Output: [4, 5]
Example 2:

Input: [5, 4, 7, 2, 3, 5, 3]
Output: [3, 5]
"""

def find_all_duplicates(nums):
  i = 0
  while i < len(nums):
    j = nums[i] - 1
    if nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]  # swap
    else:
      i += 1

  duplicateNumbers = []
  for i in range(len(nums)):
    if nums[i] != i + 1:
      duplicateNumbers.append(nums[i])

  return duplicateNumbers


def main():
  print(find_all_duplicates([3, 4, 4, 5, 5]))
  print(find_all_duplicates([5, 4, 7, 2, 3, 5, 3]))

main()

#Time complexity #
#The time complexity of the above algorithm is O(n).

#Space complexity #
#Ignoring the space required for storing the duplicates, the algorithm runs in constant space O(1).#
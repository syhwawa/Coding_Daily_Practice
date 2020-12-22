## 41. First Missing Positive
"""
Given an unsorted integer array nums, find the smallest missing positive integer.

Follow up: Could you implement an algorithm that runs in O(n) time and uses constant extra space.?

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
"""

class Solution:
    def firstMissingPositive(self, A: List[int]) -> int:
        # write your code in Python 3.6
        A.sort()
        if not A:
            return 1
        if A[-1] < 0:
            return 1
        for i in range(1, len(A) + 1):
            if i not in A:
                return i
        return A[-1] + 1
        
Time Complexity: O(N**2)

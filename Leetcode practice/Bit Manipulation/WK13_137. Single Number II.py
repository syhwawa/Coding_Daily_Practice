"""
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99

Follow up: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""

```Python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashtable = {}
        
        for i in nums:
            if i not in hashtable:
                hashtable[i] = 1
            else:
                hashtable[i] += 1
                
        for key, val in hashtable.items():
            if val == 1:
                return key

```Python
from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        if len(nums) == 1:
            return nums[0]
        for i in c:
            if c[i] == 1:
                return i

```

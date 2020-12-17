Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4


```Python
Solution 1:
class Solution:
    def singleNumber(self, nums): 
        a = 0
        for i in nums:
            a = a ^ i
        return a
```
# TC：O（N）
# SC：O（1）

```Python
Solution 2:
Using Hashtable
class Solution:
    def singleNumber(self, nums): 
        hash_table = defaultdict(int)
        for i in nums:
            hash_table[i] += 1
        for i in hash_table:
            if hash_table[i] == 1:
                return i
```

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

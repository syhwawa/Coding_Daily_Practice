Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

空间复杂度：O(N)
时间复杂度：O(N)
```Python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return []
        
        hashtable = {}
        
        for index, values in enumerate(nums):
            if target - values in hashtable:
                return [hashtable[target - values]+1, index+1]
            hashtable[values]= index
```
双指针
空间复杂度：O(N)
时间复杂度：O(1)

```Python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) -1 
        while right >= left:
            sum_target = nums[left]+ nums[right]
            if sum_target < target:
                left += 1
            elif sum_target == target:
                return [left + 1, right+ 1]
            else:
                right -= 1
        return []     
```



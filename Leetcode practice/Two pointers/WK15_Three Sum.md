Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]


```Python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Three pointers combined with sorted array
        # sorted array which helps to skip the same nums in the array
        nums.sort()
        res = []
        n = len(nums)
        if (not nums or n < 3):
            return []
        
        for i in range(n):
            if nums[i] > 0: return res 
            # skip the same nums
            if (i > 0 and nums[i] == nums[i-1]):
                continue

            l, r = i + 1, n -1

            while r > l:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    res.append([nums[i],  nums[l], nums[r]])
                    # skip the same nums, r > l is epecially for the special case [0,0,0]
                    while r > l and nums[l] == nums[l+1]:
                        l += 1
                    while r > l and nums[r] == nums[r-1]:
                        r -= 1
                    #move the new position
                    l += 1
                    r -= 1
                
                elif s < 0:
                    l += 1
                else:
                    r -= 1

        return res
 ```
 https://leetcode-cn.com/problems/3sum/solution/pai-xu-shuang-zhi-zhen-zhu-xing-jie-shi-python3-by/
复杂度分析
时间复杂度：O(n^2)
空间复杂度：O(1)

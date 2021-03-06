"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""
#暴力解法

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        from collections import Counter
        c = Counter(nums)
        return [key for key, values in c.items() if values == 2]



def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            loc = abs(nums[i]) - 1
            if nums[loc] < 0:
                res.append(loc + 1)
            nums[loc] = - nums[loc]
            
        return res


#https://leetcode-cn.com/problems/find-all-duplicates-in-an-array/solution/fu-shu-suo-yin-hao-by-powcai/

#Space COmplexity = O(1)
#Time Complexity = O(n)

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        print(nums)
        res = []
        for k in range(len(nums)):
            if nums[k] != k + 1:
                res.append(nums[k])
        return res

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

Solution: 
using Hashmap

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for index, values in enumerate(nums):
            if hash.get(target -values) is not None:
                return [index, hash.get(target-values)]
            hash[values]= index
            
      
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for idx, value in enumerate(nums):
            if (target - value) in hashtable:
                return [idx, hashtable[target-value]]
            hashtable[nums[idx]] = idx
        return []
    
    TC: O(N) N the number in array, each num cost O(1) for searching
    SC: O(N) space for hashtable

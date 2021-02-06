Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. 

Return the sum of the three integers. You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

import math
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        smallest_diff = math.inf
        
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            
            while (right > left):
                target_diff = target - nums[i] - nums[left] - nums[right]
                
                if target_diff == 0: #we've found the exact sum
                    return target
                
                # Update the smallest 
                if abs(target_diff) < abs(smallest_diff) or (abs(target_diff) == abs(smallest_diff) and target_diff > smallest_diff):
                    smallest_diff = target_diff

                if target_diff > 0:
                    left += 1
                else:
                    right -= 1
        return target - smallest_diff
    
    # Time Complexity: O(Nlong(N)) + O(N**2)
    # Space Complexity : O(N) required for sorting
    
        
        

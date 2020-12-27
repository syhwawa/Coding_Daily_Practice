Given an array of n integers nums and an integer target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

Follow up: Could you solve it in O(n2) runtime?

 

Example 1:

Input: nums = [-2,0,1,3], target = 2
Output: 2
Explanation: Because there are two triplets which sums are less than 2:
[-2,0,1]
[-2,0,3]
Example 2:

Input: nums = [], target = 0
Output: 0
Example 3:

Input: nums = [0], target = 0
Output: 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-smaller
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums)-1
            while right > left:
                target_diff = target - nums[i] - nums[left] - nums[right]
                if target_diff > 0:
                    count += right - left #Counted the all of required array in sorted nums
                    left += 1
                else:
                    right -= 1
        return count
    # Time Complexity: O(Nlong(N) + O(N^2))
    # Space Complexity: O(N) beacuse of sorting

        

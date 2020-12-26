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


def search_triplets(arr):
  arr.sort()
  triplets = []
  for i in range(len(arr)):
    if i > 0 and arr[i] == arr[i-1]:  # skip same element to avoid duplicate triplets
      continue
    search_pair(arr, -arr[i], i+1, triplets)

  return triplets


def search_pair(arr, target_sum, left, triplets):
  right = len(arr) - 1
  while(left < right):
    current_sum = arr[left] + arr[right]
    if current_sum == target_sum:  # found the triplet
      triplets.append([-target_sum, arr[left], arr[right]])
      left += 1
      right -= 1
      while left < right and arr[left] == arr[left - 1]:
        left += 1  # skip same element to avoid duplicate triplets
      while left < right and arr[right] == arr[right + 1]:
        right -= 1  # skip same element to avoid duplicate triplets
    elif target_sum > current_sum:
      left += 1  # we need a pair with a bigger sum
    else:
      right -= 1  # we need a pair with a smaller sum


def main():
  print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
  print(search_triplets([-5, 2, -1, -2, 3]))


main()

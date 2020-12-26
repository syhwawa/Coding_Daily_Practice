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


class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        triplets = []
        for i in range(len(arr)):
            right = len(arr) - 1
            left = i + 1
            if i > 0 and arr[i] == arr[i-1]:  # skip same element to avoid duplicate triplets
                continue
                
            while(left < right):
                total_sum = arr[left] + arr[right] + arr[i]
                if total_sum == 0:  # found the triplet
                    triplets.append([arr[i], arr[left], arr[right]])
                    left += 1
                    right -= 1
                    
                    while left < right and arr[left] == arr[left - 1]:
                        left += 1  # skip same element to avoid duplicate triplets
                        
                    while left < right and arr[right] == arr[right + 1]:
                        right -= 1  # skip same element to avoid duplicate triplets
        
                elif total_sum < 0:
                    left += 1  # we need a pair with a bigger sum
                else:
                    right -= 1  # we need a pair with a smaller sum

        return triplet
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

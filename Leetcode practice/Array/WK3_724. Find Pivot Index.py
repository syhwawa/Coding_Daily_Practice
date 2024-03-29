"""
Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.

Example 1:

Input: 
nums = [1, 7, 3, 6, 5, 6]
Output: 3
Explanation: 
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
Also, 3 is the first index where this occurs.
 

Example 2:

Input: 
nums = [1, 2, 3]
Output: -1
Explanation: 
There is no index that satisfies the conditions in the problem statement.
 

Note:

The length of nums will be in the range [0, 10000].
Each element nums[i] will be an integer in the range [-1000, 1000].
"""

def pivotIndex(nums):
    sum_left, sum_right = 0, sum(nums)
    for index, num in enumerate(nums): 
        sum_right -= num
        if sum_left == sum_right:
            return index
        sum_left += num
    return -1
"""
Time C O(N)
Space C O(1)
设置两个变量left和right，一个记录从左边开始的和，一个记录从右边开始的和。
当遍历的时候，中心索引左边的和即left,中心索引右边的和即right，左边和右边不相等时，遍历进入数组的下一项，left增加一项，right减少一项。

看代码的话，由两次遍历数组组成。首先需要遍历从第二项到最后一项的和，记录在right里。left是0。此时假定的中心索引为第一项。

第二次遍历即判断left是否等于right，不相等进入数组的下一项，left需要增加这一项的和，right需要减少下一项的和。

最开头和最后做了针对数组长度为0以及中心索引在最后的处理。
"""

def pivotIndex(nums):
    total = sum(nums)
    part_sum = 0
    for i, j in enumerate(nums):
        if part_sum == (total - j) / 2:
            return i
        part_sum += j3
    return -1


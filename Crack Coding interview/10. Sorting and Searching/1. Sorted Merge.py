Leetcode: 88
You are given two sorted arrays, A and B, where A has a large enough buffer at the end to hold B. Write a method to merge B into A in sorted order.

Initially the number of elements in A and B are m and n respectively.

Example:

Input:
A = [1,2,3,0,0,0], m = 3
B = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        i = len(A) - 1 #A数组里最后一个元素（最大的元素）开始比较
        while n > 0 and m > 0:
            if B[n-1] > A[n-1]: # 如果B的最后一个元素（B的最大值）大于A的最大值，则把B的这个值放到A的当前位置
                A[i] = B[n-1]# 更新B的最最大值索引
                n -= 1
            else:
                A[i] = A[n-1]
                m -= 1# 更新A的最大值索引
            i -= 1
        for j in range(n):# 要注意，如果上述循环完后，B里面还有数据，或者B还没有遍历到0，则说明B里面剩下的元素都小于A的最小元素，需要把这些元素放到A
            A[j] = B[j]

        return A 
        # Time complexity: O(m+n)
        # Space Compexity: O(1)

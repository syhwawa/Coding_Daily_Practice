"""
Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.
Example 1:

Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
Output: [1,5]
Explanation: Only 1 and 5 appeared in the three arrays.
Example 2:

Input: arr1 = [197,418,523,876,1356], arr2 = [501,880,1593,1710,1870], arr3 = [521,682,1337,1395,1764]
Output: []
 
Constraints:

1 <= arr1.length, arr2.length, arr3.length <= 1000
1 <= arr1[i], arr2[i], arr3[i] <= 2000
"""

#Solution 1:
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        return sorted(list(set(arr1) & set(arr2) & set(arr3)))
 
#Solution 2: 
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        i1,i2,i3 =0,0,0
        L = len(arr1)
        result = []
        while i1<L and i2<L and i3<L:
            if arr1[i1]== arr2[i2] and arr1[i1]==arr3[i3]:
                result.append(arr1[i1])
                i1+=1
                i2+=1
                i3+=1
            else:
                if arr1[i1] <= arr2[i2] and arr1[i1] <= arr3[i3]:
                    i1 += 1
                elif arr2[i2] <= arr1[i1] and arr2[i2] <= arr3[i3]:
                    i2 += 1
                elif arr3[i3] <= arr1[i1] and arr3[i3] <= arr2[i2]:
                    i3 += 1
        return result

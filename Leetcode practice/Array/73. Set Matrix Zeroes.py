Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
 

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        column = len(matrix[0])
        row_zero = [False for i in range(row)]
        column_zero = [False for i in range(column)]
        
        #
        for i in range(row):
            for j in range(column):
                if matrix[i][j] == 0:
                    row_zero[i] = True
                    column_zero[j] = True
        
        for i in range(row):
            for j in range(column):
                if row_zero[i] or column_zero[j]:
                    matrix[i][j] = 0
        
        # TC: O(M x N)
        # SC: O(M + N)
        


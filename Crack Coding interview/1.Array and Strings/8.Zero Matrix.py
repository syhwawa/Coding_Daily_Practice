# Leetcode 73
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0.
Hints:#17, #74, #702

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

def setZeroes(matrix):
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
    return matrix

    # TC: O(M x N)
    # SC: O(M + N)
print(setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))   

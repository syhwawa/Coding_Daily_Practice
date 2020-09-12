```Python
class Solution:
    def gridGame(self, grid, k, rules):
        if not grid or grid == []: return grid
        if len(grid) == 0 or len(grid[0]) == 0: return grid
        rules = set(rules)
        
        for i in range(k):
            grid = self.updateGrid(grid, rules)
        
        return grid
    
    def updateGrid(self, grid, rules):
        m, n = len(grid), len(grid[0])
        new_grid = [[0 for _ in range(n)] for _ in range(m)]
        directions = [(1,0),(0,1),(-1,0),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]
        
        for i in range(m):
            for j in range(n):
                count = 0
                for di, dj in directions:
                    if 0 <= i + di < m and 0 <= j + dj < n and grid[i+di][j+dj] == 1:
                        count += 1
                if count in rules: new_grid[i][j] = 1
        
        return new_grid

s = Solution()
grid = [[0,1,1,0], [1,1,0,0]]
k = 2
rules = [3,5]

print(s.gridGame(grid, k, rules))
```

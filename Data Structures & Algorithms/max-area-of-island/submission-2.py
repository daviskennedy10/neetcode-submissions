class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        biggest = 0

        row = len(grid)
        col = len(grid[0])

        def dfs(r,c, count):
            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == 0:
                return
            
            if grid[r][c] == 1:
                count[0] +=1
                grid[r][c] = 0
            
            dfs(r+1,c, count)
            dfs(r-1,c,count)
            dfs(r,c+1,count)
            dfs(r,c-1,count)
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    count = [0] * 1
                    dfs(r,c, count)
                    biggest = max(biggest, count[0])

        return biggest
            

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        row = len(grid)
        col = len(grid[0])
        #visited = [[False] * col for _ in range(row)]
        
        def dfs(r,c):
            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == "0":
                return
            if grid[r][c] == "1":
                grid[r][c] = "0"

            #visited[r][c] = False
            dfs(r+1,c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
            
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    dfs(r,c)
                    count +=1
        return count
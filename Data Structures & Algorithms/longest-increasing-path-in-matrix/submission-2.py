class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        row, col = len(matrix), len(matrix[0])
        maxLen = 0
        memo = {}


        def check(r,c,nr,nc):
            if nr < 0 or nr >= row or nc < 0 or nc >= col:
                return 0

            if matrix[r][c] < matrix[nr][nc]:
                return dfs(nr,nc)
            return 0
        def dfs(r,c):
            if r < 0 or r >= row or c < 0 or c >= col:
                return 0
            if (r,c) in memo:
                return memo[(r,c)]
            up = check(r,c,r+1,c)
            down = check(r,c,r-1,c)
            right = check(r,c,r,c+1)
            left = check(r,c,r,c-1)
            memo[(r,c)] = 1 + max(up,down,right,left)
            return memo[(r,c)]
        for r in range(row):
            for c in range(col):
                count = dfs(r,c)
                maxLen = max(maxLen, count)
        return maxLen

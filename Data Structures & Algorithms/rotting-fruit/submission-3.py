class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        q = deque()
        visited = set()
        total = 0

        def addOrange(r,c):
            if r < 0 or r >= row or c < 0 or c >= col or (r,c) in visited or grid[r][c] == 0 or grid[r][c] == 2:
                return
            q.append((r,c))
            visited.add((r,c))

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2 or grid[r][c] == 1:
                    total +=1
                if grid[r][c] == 2:
                    q.append((r,c))
        if len(q) == 0 and total == 0:
            return 0
        minute = -1
        count = 0
        while q:
            for i in range(len(q)):
                value = q.popleft()
                r = value[0]
                c = value[1]
                grid[r][c] = 2
                count += 1
                addOrange(r+1,c)
                addOrange(r-1,c)
                addOrange(r,c+1)
                addOrange(r,c-1)
            minute +=1
        if count < total:
            return -1
        else:
            return minute
                
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row = len(grid)
        col = len(grid[0])
        q = deque()
        visited = set()

        def addRoom(r,c):
            if r < 0 or r >= row or c < 0 or c >= col or (r,c) in visited or grid[r][c] == -1:
                return
            q.append((r,c))
            visited.add((r,c))
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))
        
        count = 0
        while q:
            for i in range(len(q)):
                value = q.popleft()
                r = value[0]
                c = value[1]
                grid[r][c] = count
                addRoom(r+1,c)
                addRoom(r-1,c)
                addRoom(r,c+1)
                addRoom(r,c-1)
            count += 1

                


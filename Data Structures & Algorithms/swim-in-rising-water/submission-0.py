class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = set()
        row = len(grid)
        col = len(grid[0])
        minHeap = []
        heapq.heappush(minHeap, (grid[0][0],0,0))
        time = 0

        def addtoHeap(nr,nc,minHeap,t,r,c):
            if nr < 0 or nr >= row or nc < 0 or nc >= col or (nr,nc) in visited:
                return
            next_time = max(t, grid[nr][nc])
            heapq.heappush(minHeap, (next_time,nr,nc))
        while minHeap:
            data = heapq.heappop(minHeap)
            time,r,c = data[0],data[1],data[2]
            if r == row-1 and c == col-1:
                return time
            if (r,c) in visited:
                continue
            visited.add((r,c))
            
            addtoHeap(r+1,c,minHeap,time,r,c)
            addtoHeap(r-1,c,minHeap,time,r,c)
            addtoHeap(r,c+1,minHeap,time,r,c)
            addtoHeap(r,c-1,minHeap,time,r,c)
            
        return 0
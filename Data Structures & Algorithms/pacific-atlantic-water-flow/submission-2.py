class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row = len(heights)
        col = len(heights[0])
        res = []
        pacific = set()
        atlantic = set()
        pq = deque()
        aq = deque()
        def addHeight(r,c,q,prev,container):
            if r < 0 or r >= row or c < 0 or c >= col or (r,c) in container or heights[r][c] < prev:
                return
            q.append((r,c))
            container.add((r,c))


        for r in range(row):
            for c in range(col):
                if r == 0 or c == 0:
                    pq.append((r,c))
                    pacific.add((r,c))
                if r == row-1 or c == col-1:
                    aq.append((r,c))
                    atlantic.add((r,c))
        def bfs(container, q):
            while q:
                value = q.popleft()
                r = value[0]
                c = value[1]
                
                prev = heights[r][c] 
                addHeight(r+1,c,q,prev,container)
                addHeight(r-1,c,q,prev,container)
                addHeight(r,c+1,q,prev,container)
                addHeight(r,c-1,q,prev,container)
        bfs(pacific, pq)
        bfs(atlantic,aq)
        for hei in pacific:
            if hei in atlantic:
                res.append(list(hei))
        return res
                

        

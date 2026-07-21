class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row = len(heights)
        col = len(heights[0])
        res = []
        pacific = set()
        atlantic = set()
        pq = deque()
        aq = deque()
        avisited = set()
        pvisited = set()
        def addHeight(r,c,q,prev,check):
            if r < 0 or r >= row or c < 0 or c >= col or (r,c) in check or heights[r][c] < prev:
                return
            q.append((r,c))
            check.add((r,c))

        for r in range(row):
            for c in range(col):
                if r == 0 or c == 0:
                    pq.append((r,c))
                if r == row-1 or c == col-1:
                    aq.append((r,c))
        def bfs(container, q, check):
            while q:
                value = q.popleft()
                r = value[0]
                c = value[1]
                container.add((r,c))
                prev = heights[r][c] 
                addHeight(r+1,c,q,prev,check)
                addHeight(r-1,c,q,prev,check)
                addHeight(r,c+1,q,prev,check)
                addHeight(r,c-1,q,prev,check)
        bfs(pacific, pq, pvisited)
        bfs(atlantic,aq, avisited)
        for hei in pacific:
            if hei in atlantic:
                res.append(list(hei))
        return res
                

        

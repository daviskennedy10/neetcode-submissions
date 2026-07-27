class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        minHeap = []
        heapq.heappush(minHeap, (0,points[0]))
        res =0
        while len(visited) < len(points):
            data = heapq.heappop(minHeap)
            dist = data[0]
            point = data[1]
            x,y = point[0], point[1]
            if (x,y) in visited:
                continue
            res += dist
            visited.add((x,y))
            for u,v in points:
                dist = abs(u - x) + abs(v - y)
                if dist == 0:
                    continue
                heapq.heappush(minHeap, (dist,(u,v)))
        return res   


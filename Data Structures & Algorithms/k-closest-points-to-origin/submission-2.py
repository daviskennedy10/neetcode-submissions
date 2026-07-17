class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for x,y in points:
            distance = -(x**2 + y**2)
            heapq.heappush(maxHeap, (distance, [x,y]))

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        return [point for dist, point in maxHeap]

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) <= 1:
            return stones[0]
        maxHeap = []
        for stone in stones:
            heapq.heappush(maxHeap, -stone)
        while len(maxHeap) > 1:
            first = -heapq.heappop(maxHeap)
            second = -heapq.heappop(maxHeap)
            difference = first - second
            if difference != 0:
                heapq.heappush(maxHeap, -difference)
            if difference == 0 and len(maxHeap) < 1:
                heapq.heappush(maxHeap, -0)
        return -maxHeap[0]
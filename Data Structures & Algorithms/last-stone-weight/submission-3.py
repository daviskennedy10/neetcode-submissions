class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            first = -heapq.heappop(maxHeap)
            second = -heapq.heappop(maxHeap)
            difference = first - second
            if difference != 0:
                heapq.heappush(maxHeap, -difference)

        return -maxHeap[0] if maxHeap else 0
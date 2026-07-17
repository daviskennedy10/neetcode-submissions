class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.max_heap = []
        self.k = k
        for num in nums:
            heapq.heappush(self.max_heap, num)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.max_heap, val)
        while len(self.max_heap) > self.k:
            heapq.heappop(self.max_heap)

        
        return self.max_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
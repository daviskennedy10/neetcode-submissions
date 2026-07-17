class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        heapq.heapify(self.minHeap)
        heapq.heapify(self.maxHeap)




    def addNum(self, num: int) -> None:
        if self.minHeap and num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)
        if len(self.maxHeap) - len(self.minHeap) > 1 :
            heapq.heappush(self.minHeap,  -heapq.heappop(self.maxHeap))
        if len(self.minHeap) - len(self.maxHeap) > 1 :
            heapq.heappush(self.maxHeap,  -heapq.heappop(self.minHeap))

    def findMedian(self) -> float:
        if len(self.minHeap) > len(self.maxHeap):
            return float(self.minHeap[0])
        elif len(self.maxHeap) > len(self.minHeap):
            return float(-self.maxHeap[0])
        else:
            return (self.minHeap[0]+(-self.maxHeap[0])) / 2.0



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
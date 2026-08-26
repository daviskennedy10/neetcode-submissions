"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        count = 1
        n = len(intervals)
        if n == 1:
            return count
        if n < 1:
            return 0
        intervals.sort(key=lambda x: x.start)
        prev = intervals[0]
        minHeap = []
        heapq.heapify(minHeap)
        heapq.heappush(minHeap,prev.end)

        for i in range(1,n):
            start = intervals[i].start
            end = intervals[i].end
            if start >= minHeap[0]:
                heapq.heappop(minHeap)
                
            else:
                count +=1
            heapq.heappush(minHeap, end)
        return count
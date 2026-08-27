class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        n = len(intervals)
        sort_q = []
        res = [-1] * len(queries)
        minHeap = []
        heapq.heapify(minHeap)
        for i,q in enumerate(queries):
            sort_q.append([q,i])
        sort_q.sort()
        intervals.sort()
        j = 0
        for i in range(len(sort_q)):
            query = sort_q[i][0]
            idx = sort_q[i][1]
            
            while j < n and intervals[j][0] <= query:
                difference = intervals[j][1] - intervals[j][0] + 1
                use = [difference, intervals[j][1]]
                heapq.heappush(minHeap, use)
                j +=1
            while minHeap and minHeap[0][1] < query:
                heapq.heappop(minHeap)
                
            if minHeap:
                res[idx] = minHeap[0][0]
                    
        return res
                
        

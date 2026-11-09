class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = []
        maxHeap = []
        if a > 0:
            heapq.heappush(maxHeap, [-a,"a"])
        if b > 0:
            heapq.heappush(maxHeap, [-b,"b"])
        if c > 0:
            heapq.heappush(maxHeap, [-c,"c"])
        
        while maxHeap:
            high = heapq.heappop(maxHeap)
            
            if len(res) >= 2 and high[1] == res[-1] and high[1] == res[-2]:
                if maxHeap:
                    second = heapq.heappop(maxHeap)
                    second[0] = -second[0]
                    res.append(second[1])
                    second[0] -= 1
                    heapq.heappush(maxHeap,high)
                    if second[0] > 0:
                        # put it back in
                        
                        heapq.heappush(maxHeap,[-second[0], second[1]])
            else:
                high[0] = -high[0]
                res.append(high[1])
                high[0] -=1
                if high[0] > 0:
                    # put it back in 
                    heapq.heappush(maxHeap,[-high[0], high[1]])
            
        
        final = "".join(res)
        return final

            
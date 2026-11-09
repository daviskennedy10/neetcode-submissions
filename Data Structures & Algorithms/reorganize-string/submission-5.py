class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        freq = Counter(s)
        word = []
        use_list = []
        res = []

        for k,v in freq.items():
            use_list.append([v,k])

        maxheap = []
        for v,k in use_list:
            heapq.heappush(maxheap, [-v,k])
        highest = -maxheap[0][0]
        if highest > (n+1)//2:
            return ""
        
        add = False
        if maxheap:
            high = heapq.heappop(maxheap)
            highest = -high[0]
            res.append(high[1])
            highest -= 1

            if highest >= 1:
                put_back = [-highest,high[1]]
                add = True

        while maxheap:
            high = heapq.heappop(maxheap)
            highest = -high[0]
            res.append(high[1])
            highest -=1
            if add:
                heapq.heappush(maxheap, put_back)
            if highest >= 1:
                put_back = [-highest,high[1]]
                add = True
            else:
                add = False

        final = "".join(res)
        return final
            


        


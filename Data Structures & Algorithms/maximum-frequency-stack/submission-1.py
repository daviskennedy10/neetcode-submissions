class FreqStack:

    def __init__(self):
        # create max heap
        self.maxheap = []
        # create map
        self.freq = {}
        self.index = 0
        

    def push(self, val: int) -> None:
        # add its frequency to map with its key
        self.freq[val] = self.freq.get(val,0) + 1
        n = len(self.maxheap)
        # create a pair (freq, val)
        self.index+=1
        element = (-self.freq[val], -self.index, val)

        # if the pair with previous count exists in heap remove it (freq-1, val)
        heapq.heappush(self.maxheap, element)
        # add it to the heap
    
        

    def pop(self) -> int:
        # store variable for freq
        # check if it exists in map:
            # store the freq from map in freq
        # obtain the first element from the maxheap
        element = heapq.heappop(self.maxheap)
        count = -element[0]
        val = element[2]
        if val in self.freq:
            self.freq[val]-=1
    
        return val
        # res is the pair[1]
        # if pair[0] == 1:
            # pop it from the heap
        # else :
            # pair[0]--
            # put the new pair back in the heap
        # return res

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
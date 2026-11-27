class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        q = deque()
        for i in range(len(tickets)):
            element = [tickets[i],i]
            q.append(element)

        while q:
            time +=1
            first = q.popleft()
            first[0]-=1
            if first[0] > 0:
                q.append(first)
            elif first[0] == 0 and first[1] == k:
                return time
        
        return time

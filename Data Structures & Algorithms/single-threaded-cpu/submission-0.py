class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        time = 0
        minheap = []
        res = []
        new_tasks = []
        n = len(tasks)
        for i in range(len(tasks)):
            new_tasks.append(tasks[i]+[i])
        sorted_tasks = sorted(new_tasks, key=lambda x:x[0])
        i = 0

        while i < n or minheap:
            if not minheap and time < sorted_tasks[i][0]:
                time = sorted_tasks[i][0]

            while i < n and sorted_tasks[i][0] <= time:
                heapq.heappush(minheap,[sorted_tasks[i][1],sorted_tasks[i][2]])
                i+=1
            
            ready = heapq.heappop(minheap)
            time += ready[0]
            res.append(ready[1])
            



        
        return res
                

            
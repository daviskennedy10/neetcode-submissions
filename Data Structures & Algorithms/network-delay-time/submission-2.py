class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjMap = {i:[] for i in range(1, n+1)}

        for member in times:
            node, target, time = member[0], member[1], member[2]

            adjMap[node].append((time, target))

        minHeap = []
        visited = set()
        heapq.heappush(minHeap, (0,k))
        max_time = 0
        keep = [0] * 2
        while minHeap:
            for _ in range(len(minHeap)):
                time, node = heapq.heappop(minHeap)
                members = adjMap[node]
                if node in visited:
                    continue
                visited.add(node)
                max_time = time
                if len(visited) == n:
                    max_time
                for member in members:
                    weight = member[0]
                    target = member[1]
                    heapq.heappush(minHeap, (time+weight,target))
        if len(visited) == n:
            return max_time
        else:
            return -1
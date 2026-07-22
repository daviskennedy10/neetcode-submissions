class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjMap = {i:[] for i in range(n)}
        for u,v in edges:
            adjMap[u].append(v)
            adjMap[v].append(u)
        
        visited = set()
        count = set()
        total = 0
        def dfs(node, parent):
            if node in visited:
                return
            visited.add(node)
            
            for child in adjMap[node]:
                if node == parent:
                    continue
                dfs(child, node)
            return
        for i in range(n):
            if i not in visited:
                total +=1
                if i > 0:
                    dfs(i, i-1)
                else:
                    dfs(i,-1)
        return total
                
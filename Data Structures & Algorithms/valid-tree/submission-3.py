class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjMap = {i:[] for i in range(n)}
        if len(edges) - n != -1:
            return False

        for u,v in edges:
            adjMap[u].append(v)
            adjMap[v].append(u)
        visited = set()
        
        def dfs(node, parent):
        
            if node in visited:
                return False
            visited.add(node)
            
            for child in adjMap[node]:
                if child == parent:
                    continue
                if not dfs(child, node):
                    return False
            
            return True
        
        if not dfs(0,-1):
            return False
        return len(visited) == n
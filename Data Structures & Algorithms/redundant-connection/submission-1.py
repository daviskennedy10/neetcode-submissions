class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adjMap = {i:[] for i in range(1, n+1)}

    
        def canReach(u, v, visited):
            if u == v:
                return True
    
            visited.add(u)
            for child in adjMap[u]:
                if child not in visited:
                    if canReach(child,v,visited):
                        return True
            
            return False
        
        for u,v in edges:
            if canReach(u,v, set()):
                return [u,v]
            else:
                adjMap[u].append(v)
                adjMap[v].append(u) 
        return []
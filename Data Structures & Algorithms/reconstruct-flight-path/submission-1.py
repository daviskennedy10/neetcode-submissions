class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {src:[] for src,dst in tickets}

        tickets.sort()
        for u,v in tickets:
            adj[u].append(v)
        res = ["JFK"]
        def dfs(airport):
            if len(res) == len(tickets)+1:
                return True
            if airport not in adj:
                return False

            temp = list(adj[airport])
            for i,v in enumerate(temp):
                res.append(v)
                adj[airport].pop(i)
                if dfs(v):
                    return True
                
                res.pop()
                adj[airport].insert(i, v)
            return False
        dfs("JFK")
        return res

            


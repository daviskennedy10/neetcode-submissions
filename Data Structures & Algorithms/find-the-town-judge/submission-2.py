class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj_map = defaultdict(list)

        for u,v in trust:
            adj_map[u].append(v)
        print(adj_map)
        for i in range(1,n+1):
            found_in_all = True
            for key in adj_map:
                if i not in adj_map[key]:
                    found_in_all = False
                    break
            if found_in_all:
                return i
        return -1
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjMap = {i:[] for i in range(numCourses)}
        visited = set()
        res = []
        for crs,pre in prerequisites:
            adjMap[crs].append(pre)
        visiting, cycle = set(), set()
        
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visiting:
                return True

            cycle.add(crs)
            for prereq in adjMap[crs]:
                if dfs(prereq) == False:
                    return False
            res.append(crs)
            visiting.add(crs)
            cycle.remove(crs)
            return True
            

        for i in range(numCourses):
            if dfs(i) == False:
                return []
        return res
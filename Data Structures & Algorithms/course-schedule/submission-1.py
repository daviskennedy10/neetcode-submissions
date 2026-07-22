class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjMap = {i:[] for i in range(numCourses)}
        visited = set()

        for crs,pre in prerequisites:
            adjMap[crs].append(pre)
        
        def dfs(crs):
            if crs in visited:
                return False
            if adjMap[crs] == []:
                return True
            visited.add(crs)
            for prereq in adjMap[crs]:
                if not dfs(prereq):
                    return False
            visited.remove(crs)
            adjMap[crs] = []
            return True
        
        for j in range(numCourses):
            if not dfs(j):
                return False
        return True
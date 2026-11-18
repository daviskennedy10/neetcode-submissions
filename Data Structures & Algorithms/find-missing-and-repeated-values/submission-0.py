class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        res = []
        check = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] in check:
                    res.append(grid[i][j])
                check.add(grid[i][j])
        top = len(grid)*len(grid[0]) + 1
        for i in range(1,top):
            if i not in check:
                res.append(i)
                return res
        return res
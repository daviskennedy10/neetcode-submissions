class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()
        def dfs(idx, total):
            if total == target:
                res.append(subset.copy())
                return
            if total > target:
                return
            
            for j in range(idx, len(candidates)):
                if j > idx and candidates[j] == candidates[j-1]:
                    continue
                
                subset.append(candidates[j])
                dfs(j+1, total + candidates[j])
                subset.pop()

        dfs(0,0)
        return res
        
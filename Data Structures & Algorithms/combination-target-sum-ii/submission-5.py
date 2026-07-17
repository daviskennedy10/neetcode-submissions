class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        total = 0
        candidates.sort()

        def backtrack(i, total):
            if total == target:
                res.append(subset.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                subset.append(candidates[j])
                backtrack(j+1, total + candidates[j])
                subset.pop()
        
        backtrack(0,0)
        return res
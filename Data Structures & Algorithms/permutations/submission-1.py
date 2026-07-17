class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        visited = set()

        def dfs():
            if len(subset) == len(nums):
                res.append(subset.copy())
            
            
            for j in range(len(nums)):
                if nums[j] in visited:
                    continue
                visited.add(nums[j])
                subset.append(nums[j])
                dfs()
                subset.pop()
                visited.remove(nums[j])
        dfs()
        return res
            
        
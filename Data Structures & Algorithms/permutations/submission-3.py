class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        visited = set()

        def backtrack():
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            for j in range(len(nums)):
                if nums[j] in visited:
                    continue;
                visited.add(nums[j])
                subset.append(nums[j])
                backtrack()
                subset.pop()
                visited.remove(nums[j])
        backtrack()
        return res
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        self.total = 0

        def backtrack(i):
            if self.total == target:
                res.append(subset.copy())
                return
            if i >= len(nums) or self.total > target:
                return 
            self.total += nums[i]
            subset.append(nums[i])
            backtrack(i)
            subset.pop()
            self.total -= nums[i]
            backtrack(i+1)
        backtrack(0)
        return res
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        n = len(nums)
        dp = [0] * n
        memo = {}

        def brute(idx, prev):
            if idx == len(nums):
                return 0
            if (idx,prev) in memo:
                return memo[(idx,prev)]
            
            skip = brute(idx+1, prev)
            
            take = 0
            if nums[idx] > prev:
                take = 1 + brute(idx+1,nums[idx])
            memo[(idx,prev)] = max(skip,take)
            return max(skip,take)
        
        return brute(0,float("-inf"))
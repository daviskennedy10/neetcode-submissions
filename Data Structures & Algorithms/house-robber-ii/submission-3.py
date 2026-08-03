class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        def robLine(houses):
            n = len(houses)
            dp = [0] * n
            dp[0] = houses[0]
            for i in range(1,n):
                dp[i] = max(dp[i-2]+houses[i], dp[i-1])
            return dp[n-1]
        
        return max(robLine(nums[1:]), robLine(nums[:-1]))
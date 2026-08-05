class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        nums.sort()
        total = sum(nums)
        target = total // 2
        dp = [False] * (target+1)
        
        if total % 2 != 0:
            return False
        adder = 0
        dp[0] = True
        for num in nums:
            for j in range(target-1, -1,-1):
                if dp[j] and j+num <= target:
                    dp[j+num] = True
                

        return dp[target]
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = float("inf")
        n = len(nums)
        l = 0
        window_sum = 0
        if sum(nums) < target:
            return 0
        for r in range(n):
            if nums[r] >= target:
                return 1
            window_sum += nums[r]
            while l < r and window_sum >= target:
                minLen = min(minLen,r-l+1)
                window_sum -= nums[l]
                l+=1
            
            
        
        return minLen
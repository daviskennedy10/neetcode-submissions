class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = float("inf")
        n = len(nums)
        l = 0
        window_sum = 0
        for r in range(n):
            window_sum += nums[r]
            while window_sum >= target:
                minLen = min(minLen,r-l+1)
                window_sum -= nums[l]
                l+=1
            
            
        
        if minLen == float("inf"):
            return 0
        else:
            return minLen
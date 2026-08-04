class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        curr_min, curr_max = 1,1
        res = nums[0]

        for i in range(n):
            temp = curr_max * nums[i]
            curr_max = max(temp, curr_min * nums[i], nums[i])
            curr_min = min(temp, nums[i],curr_min * nums[i])
            res = max(res, curr_max)
            
        
        return res
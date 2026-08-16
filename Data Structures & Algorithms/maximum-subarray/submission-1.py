class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_so_far = float("-inf")
        current_max = float("-inf")
        n = len(nums)

        for i in range(n):
            current_max = max(nums[i], current_max + nums[i])
            max_so_far= max(current_max, max_so_far)
        return max_so_far
 
            

            
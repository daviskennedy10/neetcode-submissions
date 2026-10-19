class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len = float("-inf")
        n = len(nums)
        curr_len = 0
        for i in range(n):
            if nums[i] == 1:
                curr_len +=1
            else:
                curr_len = 0
            max_len = max(max_len, curr_len)
        return max_len
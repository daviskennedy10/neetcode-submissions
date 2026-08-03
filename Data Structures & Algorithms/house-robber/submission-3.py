class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        robone = 0
        robtwo = 0

        for i in range(n):
            temp = robtwo
            robtwo = max(robone + nums[i], robtwo)
            robone = temp
        return max(robone,robtwo)
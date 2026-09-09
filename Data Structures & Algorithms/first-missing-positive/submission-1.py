class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        check = set(nums)
        biggest = max(check)
        for i in range(1,biggest):
            if i not in check:
                return i
        if biggest < 0:
            return 1
        else:
            return biggest + 1
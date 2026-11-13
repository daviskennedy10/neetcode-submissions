class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        so_far = 0
        print(total)
        for i in range(len(nums)):
            
            
            use = total - nums[i]
            print(f"use: {use}")
            print(f"left_side: {so_far}")
            if so_far == use / 2:
                return i
            print(f"half_total: {use/2}")
            so_far += nums[i]

        return -1
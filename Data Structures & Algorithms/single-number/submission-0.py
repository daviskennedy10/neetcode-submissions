class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans = nums[0]
        for i in range(0,len(nums)-1):
            
            if i > 0:
                if nums[i] != nums[i+1] and nums[i-1] != nums[i]:
                    ans = nums[i]
                if i == len(nums)-2 and nums[i] != nums[i+1]:
                   ans = nums[i+1] 
        return ans
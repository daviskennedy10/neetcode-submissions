class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        l,r = 0, n-1


        while l <= r:
            if nums[l] == val:
                nums[l] = nums[r]
                r -=1
            else:
                l +=1
        return r +1
        

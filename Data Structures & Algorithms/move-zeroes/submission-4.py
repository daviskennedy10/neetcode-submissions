class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l,r = 0,1

        while r < n and l < r:
            if nums[l] != 0:
                l+=1
                r+=1
                continue
            while r < n and nums[r] == 0:
                r +=1
            if nums[l] == 0 and r < n:
                nums[l], nums[r] = nums[r], nums[l]
                r +=1
                
            l+=1

            
        
                


        
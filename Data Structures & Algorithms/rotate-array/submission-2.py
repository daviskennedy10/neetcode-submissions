class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tester = nums + nums
        n = len(nums) 
        k = k % n
        j = n - k
        i = 0
        
        for i in range(n):
            nums[i] = tester[j+i]
            
        
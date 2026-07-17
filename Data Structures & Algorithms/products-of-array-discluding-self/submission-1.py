class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n
        res=[]
        prefix[0] = 1
        suffix[n-1] = 1
        for i in range(1, n):
            prefix[i] = prefix[i-1]*nums[i-1]

        for j in range(n-2, -1, -1):
            suffix[j] = suffix[j+1] * nums[j+1]

        for s in range(n):
            res.append(prefix[s]* suffix[s])
        
        return res
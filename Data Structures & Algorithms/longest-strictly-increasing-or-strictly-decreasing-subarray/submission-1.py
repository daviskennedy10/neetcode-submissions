class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        length = 0
        maxLen = float("-inf")
        if n == 1:
            return n

        l = 0
        prev = nums[l]
        neg = False
        for r in range(n-1):
            length = 1
            j = r+1
            prev = nums[r]
            if nums[j] < prev:
                neg = True
            else:
                neg = False
            while j < n and nums[j] - prev > 0 and not neg:
                prev = nums[j]
                j+=1
                length +=1
                
            else:
                while j < n and nums[j] - prev < 0 and neg:
                    prev = nums[j]
                    j+=1
                    length +=1
            maxLen = max(length, maxLen)
        
        return maxLen

                
                


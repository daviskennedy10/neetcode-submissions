class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = l+k-1
        res = []
        placer = []
        for i in range(k):
            placer.append(nums[i])
        res.append(max(placer))    
        for r in range(k, len(nums)):
            while(r-l+1 > k):
                placer.remove(nums[l])
                l+=1
            
            placer.append(nums[r])
            res.append(max(placer))
        
        return res


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        placer = set()
        res = 0
        count = 0

        for num in nums:
            placer.add(num)

        
        for check in nums:
            if check-1 not in placer:
                count = 1

                while(check + count in placer):
                    count+=1
                res = max(count, res)
            
            
        
        return res
            



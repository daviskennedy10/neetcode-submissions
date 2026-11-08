class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        check = Counter(nums)
        for k,v in check.items():
            if v >= 2:
                res.append(k)
        for i in range(1,n+1):
            if i not in check:
                res.append(i)
        
        
        return res


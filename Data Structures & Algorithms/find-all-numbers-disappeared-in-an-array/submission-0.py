class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        checker = set(nums)
        n = len(nums)
        res = []
        for i in range(1,n+1):
            if i not in checker:
                res.append(i)
        return res


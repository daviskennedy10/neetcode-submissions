class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        n = len(nums)
        check = Counter(nums)
        for k,v in check.items():
            if v % 2 != 0:
                return False
        return True
            
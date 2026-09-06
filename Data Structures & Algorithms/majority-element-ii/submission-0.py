class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        hold = Counter(nums)
        print(hold)
        for u,v in hold.items():
            if v > n//3:
                res.append(u)
        return res

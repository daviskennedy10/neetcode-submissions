class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1, cand2 = None, None
        count1, count2 = 0,0
        n = len(nums)

        for num in nums:
            if cand1 == num:
                count1 +=1
            elif cand2 == num:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = num, 1
            elif count2 == 0:
                cand2, count2 = num, 1
            else:
                count1-=1
                count2-=1
        
        res = []
        for c in (cand1, cand2):
            if c is not None and nums.count(c) > (n//3):
                res.append(c)
        return res
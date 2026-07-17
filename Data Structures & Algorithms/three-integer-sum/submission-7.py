class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while(l < r):
                three_sum = a + nums[r]+ nums[l]
                if three_sum == 0:
                    ans = [a, nums[r], nums[l]]
                    res.append(ans)
                    l+=1
                    r-=1
                    while l < r  and nums[l] == nums[l-1]:
                        l+=1

                elif three_sum < 0:
                    l+=1
                else:
                    r-=1
        return res

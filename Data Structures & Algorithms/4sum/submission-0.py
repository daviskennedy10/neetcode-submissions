class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []

        for i in range(n):
            numA = nums[i]
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,n):
                numB = nums[j]
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                l = j+1
                r = n-1
                while l < r:
                    if nums[i] + nums[j] + nums[l] + nums[r] == target:
                        use = [nums[i], nums[j], nums[l], nums[r]]
                        res.append(use)
                        while l < r and nums[l] == nums[l+1]:
                            l +=1
                        l+=1
                        r-=1
                    elif nums[i] + nums[j] + nums[l] + nums[r] > target:
                        r -=1
                    else:
                        l +=1
        return res




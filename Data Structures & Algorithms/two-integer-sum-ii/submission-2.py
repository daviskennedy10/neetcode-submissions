class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r = len(numbers)-1
        l = 0
        res = []
        while l < r:
            if numbers[l] + numbers[r] == target:
                res.append(l+1)
                res.append(r+1)
                return res

            if numbers[l] + numbers[r] < target:
                l+=1

            if numbers[l] + numbers[r] > target:
                r-=1
        
        return res

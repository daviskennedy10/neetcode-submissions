class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}
        def dfs(i, amount):
            if i == n:
                if amount == target:
                    return 1
                else:
                    return 0
            if (i,amount) in memo:
               return memo[(i,amount)]
            
            takepos = dfs(i+1,amount+nums[i])
            takeneg = dfs(i+1, amount-nums[i])
            memo[(i,amount)] = takepos + takeneg
            count = takepos + takeneg
            return count
        
        return dfs(0,0)
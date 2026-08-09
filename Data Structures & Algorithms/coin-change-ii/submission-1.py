class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dfs(i, amount):
            if i >= len(coins) or amount < 0:
                return 0
        
            
            if amount == 0:
                return 1

            if (i,amount) in memo:
                return memo[(i,amount)]
            
            take = dfs(i,amount - coins[i])
            skip = dfs(i+1, amount)
            count = take + skip
            memo[(i,amount)] = take + skip
            return count
        return dfs(0,amount)
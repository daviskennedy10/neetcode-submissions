class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        n = len(prices)
        profit = 0

        def dfs(day, buying):
            if day >= n:
                return 0
            if (day, buying) in memo:
                return memo[(day, buying)]

            if buying:
                buy = dfs(day+1, not buying) - prices[day]
                cooldown = dfs(day+1, buying) 
                memo[(day, buying)] = max(buy, cooldown)
            else:
                sell = dfs(day+2, not buying) + prices[day]
                cooldown = dfs(day+1, buying)
                memo[(day, buying)] = max(sell, cooldown)
            return memo[(day, buying)]
        return dfs(0, True)
        

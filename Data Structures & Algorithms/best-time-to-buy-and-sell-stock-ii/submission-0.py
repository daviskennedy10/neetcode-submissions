class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        profit = 0
        n = len(prices)
        buy, sell = prices[0],0
        for i in range(n-1):
            if prices[i] > prices[i+1]:
                buy = prices[i+1]
                continue
            else:
                sell = prices[i+1]
                buy = prices[i]
            
            if sell > buy:
                profit += sell - buy
            
        return profit



            
            
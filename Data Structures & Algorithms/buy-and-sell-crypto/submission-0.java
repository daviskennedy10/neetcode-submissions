class Solution {
    public int maxProfit(int[] prices) {
        int maxProfit = 0;
        if(prices.length <= 1){
            return maxProfit;
        }
        int buyDate = 0;
        int sellDate = 1;
        int max = 0;
        for(int day = 0; day < prices.length; day++){
            if(prices[day] > max){
                max = prices[day];
            }
            if(prices[day] < prices[buyDate]){
                buyDate = day;
            }
            if(prices[day] - prices[buyDate] > maxProfit){
                maxProfit = prices[day] - prices[buyDate];
                sellDate = day;
            }

        }
        return maxProfit;
    }
}


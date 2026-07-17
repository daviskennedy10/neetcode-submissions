class Solution {
    public int maxProfit(int[] prices) {
        int maxProfit = 0;
        if(prices.length <= 1){
            return maxProfit;
        }
        int minPrice = prices[0];
        for(int i=0; i < prices.length; i++){
            minPrice = Math.min(minPrice, prices[i]);
            int diff = prices[i] - minPrice;
            maxProfit = Math.max(maxProfit, diff);
        }
        return maxProfit;
    }
}

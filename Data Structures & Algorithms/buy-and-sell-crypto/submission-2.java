class Solution {
    public int maxProfit(int[] prices) {
        int l = 0;
        int r = 1;
        int profit = 0;
        int maxP = 0;
        while(r < prices.length){
            if(prices[r] > prices[l]){
                profit = prices[r] - prices[l];
                maxP = Math.max(profit, maxP);
            }
            else{
                l = r;
            }
            r++;
        }
        return maxP;
        
        
    }
}

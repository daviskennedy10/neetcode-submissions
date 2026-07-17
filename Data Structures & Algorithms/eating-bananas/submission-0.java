class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        Arrays.sort(piles);
        int high = piles[piles.length-1];
        int low = 1;
        int time = 0;
        while(low <= high){
            int mid = (high + low)/2;
            for(int c : piles){
                double adder = Math.ceil((double)c/mid);
                time += adder;

            }
            if(time <= h){
                high = mid - 1;
                time = 0;
            }
            else{
                low = mid + 1;
                time = 0;
            }
        }
        return low;

    }
}

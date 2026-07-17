class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        int fleets = 0;
        double last = -1;
        int[][] store = new int[position.length][2];
        for(int i = 0; i < position.length; i++){
            store[i][0] = position[i];
            store[i][1] = speed[i];
        }
        Arrays.sort(store, (a,b) -> b[0] - a[0]);
        for(int j = 0; j < store.length; j++){
            double time = (double) (target - store[j][0])/ store[j][1];
            if(time > last){
                fleets++;
                last = time;
            }
            

        }
        return fleets;
    }
}

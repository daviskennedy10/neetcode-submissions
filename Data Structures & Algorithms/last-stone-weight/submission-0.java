class Solution {
    public int lastStoneWeight(int[] stones) {
        int res = 0;
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Comparator.reverseOrder());
        for(int stone : stones){
            maxHeap.offer(stone);
        }
        while(!maxHeap.isEmpty()){
            int first = maxHeap.poll();
            if(maxHeap.peek() == null){
                maxHeap.offer(first);
                break;
            }
            int second = maxHeap.poll();
            if(first == second){
                continue;
            }
            else{
                maxHeap.offer(Math.abs(first - second));
            }

        }
        if(maxHeap.isEmpty()){
            return 0;
        }
        else{
            return maxHeap.peek();
        }
    }
}

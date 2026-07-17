class KthLargest {
    PriorityQueue<Integer> minHeap;
    int num;

    public KthLargest(int k, int[] nums) {
        minHeap = new PriorityQueue<>();
        num = k;
        for(int i = 0; i < nums.length; i++){
            minHeap.offer(nums[i]);
            if(minHeap.size() > k){
                minHeap.poll();
            }
        }
    }
    
    public int add(int val) {
        minHeap.offer(val);
        if(minHeap.size() > num){
            minHeap.poll();
        }
        return minHeap.peek();
    }
}

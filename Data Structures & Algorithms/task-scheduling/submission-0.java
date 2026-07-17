class Solution {
    public int leastInterval(char[] tasks, int n) {
        int time = 0;
        if(tasks.length == 0){
            return time;
        }
        HashMap<Character, Integer> freq = new HashMap<>();
        for(char task : tasks){
            freq.put(task, freq.getOrDefault(task, 0)+ 1);
        }
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Comparator.reverseOrder());
        for(int count : freq.values()){
            maxHeap.offer(count);
        }
        Queue<int[]> cooldown = new LinkedList<>();
        while(!maxHeap.isEmpty() || !cooldown.isEmpty()){
            time++;
            if(!maxHeap.isEmpty()){
                int val = maxHeap.poll() - 1;
                if(val > 0){
                    cooldown.offer(new int[]{val, time + n});
                }
                
            }
            if(!cooldown.isEmpty() && cooldown.peek()[1] == time){
                int use = cooldown.poll()[0];
                maxHeap.offer(use);
            }
        }
        return time;


    }
}

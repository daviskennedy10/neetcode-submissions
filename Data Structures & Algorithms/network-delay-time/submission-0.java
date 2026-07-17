class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {
        Map<Integer, List<int[]>> adj = new HashMap<>();
        for(int[] time : times){
            adj.computeIfAbsent(time[0], key -> new ArrayList<>()).add(new int[]{time[1], time[2]});
        }
        PriorityQueue<int[]> minHeap = new PriorityQueue<>(Comparator.comparing(a -> a[0]));
        minHeap.offer(new int[]{0, k});
        Set<Integer> visited = new HashSet<>();
        int t = 0;
        while(!minHeap.isEmpty()){
            int[] stuff = minHeap.poll();
            int w1 = stuff[0];
            int n1 = stuff[1];
            if(visited.contains(n1)){
                continue;
            }
            visited.add(n1);
            t = w1;
            if(adj.containsKey(n1)){
                for(int[] next : adj.get(n1)){
                    int n2 = next[0];
                    int w2 = next[1];
                    if(!visited.contains(n2)){
                        minHeap.offer(new int[]{w1 + w2, n2});
                    }
                }


            }
        }
        if(visited.size() == n){
            return t;
        }
        else{
            return -1;
        }

    }
}

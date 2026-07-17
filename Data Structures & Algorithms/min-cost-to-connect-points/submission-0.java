class Solution {
    public int minCostConnectPoints(int[][] points) {
        Map<Integer, List<int[]>> adj = new HashMap<>();
        int N = points.length;
        for(int i = 0; i < N; i++){
            int x1 = points[i][0];
            int y1 = points[i][1];
            for(int j = i + 1; j < N; j++){
                int x2 = points[j][0];
                int y2 = points[j][1];

                int dist = Math.abs(x1 - x2) + Math.abs(y1 - y2);
                adj.computeIfAbsent(i, k -> new ArrayList<>()).add(new int[]{dist, j});
                adj.computeIfAbsent(j, k -> new ArrayList<>()).add(new int[]{dist, i});

            
            }
        }
        PriorityQueue<int[]> minHeap = new PriorityQueue<>(Comparator.comparing(a ->a[0]));
        minHeap.offer(new int[]{0,0});
        Set<Integer> visited = new HashSet<>();
        int res = 0;
        while(visited.size() != N){
           int[] path = minHeap.poll();
           int distance = path[0];
           int node = path[1];

           if(visited.contains(node)){
            continue;
           }
           res += distance;
           visited.add(node);
           if(adj.containsKey(node)){
            for(int[] edge : adj.getOrDefault(node, new ArrayList<>())){
                int nextD = edge[0];
                int nextN = edge[1];
                minHeap.offer(new int[]{nextD, nextN});
            }
           }
        }
        return res;
    }
}

class Solution {
    List<List<Integer>> adj;
    Set<Integer> visited;
    int count;
    public int countComponents(int n, int[][] edges) {
        adj = new ArrayList<>();
        visited = new HashSet<>();
        count = 0;
        for(int i = 0; i < n; i++){
            adj.add(new ArrayList<>());
        }
        for(int[] edge : edges){
            adj.get(edge[0]).add(edge[1]);
            adj.get(edge[1]).add(edge[0]);
        }
        for(int j = 0; j < n; j++){
            if(!visited.contains(j)){
                dfs(j);
                count++;
            }
        }
        return count;

    }
    private void dfs(int node){
        if(visited.contains(node)){
            return;
        }
        visited.add(node);
        for(int connection : adj.get(node)){
            dfs(connection);
        }
        return;
    }
}

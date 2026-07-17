class Solution {
    Set<Integer> visit ;
    Set<Integer> visited;
    List<List<Integer>> adj;
    public boolean validTree(int n, int[][] edges) {
        if(edges.length > n - 1){
            return false;
        }
        visit = new HashSet<>();
        visited = new HashSet<>();
        adj = new ArrayList<>();
        for(int i = 0; i < n; i++){
            adj.add(new ArrayList<>());
        }
        for(int[] edge : edges){
            adj.get(edge[0]).add(edge[1]);
            adj.get(edge[1]).add(edge[0]);
        }
        /**Queue<Integer> q = new LinkedList<>();
        for(int t = 0; t < adj.size(); t++){
            if(adj.get(t).isEmpty()){
                return false;
            }
        }
        int finished = 0;
        while(!q.isEmpty()){
            int 
        } */
        
        if(!dfs(0, -1)){
            return false;
        }
        return visited.size() == n;

    }
    private boolean dfs(int node, int parent){
        if(visited.contains(node)){
            return false;
        } 
        visited.add(node);
        for(int children : adj.get(node)){
            if(children == parent){
                continue;
            }
            if(!dfs(children, node)){
                return false;
            }
        }
        return true;
    }
}

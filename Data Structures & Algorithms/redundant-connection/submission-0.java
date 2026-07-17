class Solution {
    int[] parent;
    int[] rank;
    public int[] findRedundantConnection(int[][] edges) {
        int n = edges.length;
        parent = new int[n+ 1];
        rank = new int[n+1];
        for(int i = 0; i < n; i++){
            parent[i] = i;
            rank[i] = 1;
        }

        for(int[] edge : edges){
            if(!union(edge[0], edge[1])){
                return new int[]{edge[0],edge[1]};
            }
        }
        return new int[]{};
    }
    private int find(int n){
        int p = parent[n];
        while(p != parent[p]){
            parent[p] = parent[parent[p]];
            p = parent[p];
        }
        return p;
    }
    private boolean union(int p, int q){
        int p1 = find(p);
        int p2 = find(q);

        if(p1 == p2){
            return false;
        }
        if(rank[p1] > rank[p2]){
            parent[p2] = p1;
            rank[p1] += rank[p2];
        }
        else{
            parent[p1] = p2;
            rank[p2] += rank[p1];
        }
        return true;

    }
}

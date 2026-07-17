class Solution {
    int rows;
    int cols;
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        List<List<Integer>> res = new ArrayList<>();
        Set<Pair<Integer, Integer>> pacSet = new HashSet<>();
        Set<Pair<Integer, Integer>> atlSet = new HashSet<>();
        Queue<int[]> pacQ = new LinkedList<>();
        Queue<int[]> atlQ = new LinkedList<>();
        rows = heights.length;
        cols = heights[0].length;
        for(int i = 0; i < rows; i++){
            for(int j = 0; j < cols; j++){
                if(i == 0 || j == 0){
                    pacQ.offer(new int[]{i,j});
                    pacSet.add(new Pair<>(i,j));
                }
                if(j == cols-1 || i == rows-1){
                    atlQ.offer(new int[]{i,j});
                    atlSet.add(new Pair<>(i,j));

                }
            }
        }
        bfs(pacQ, pacSet, heights);
        bfs(atlQ, atlSet, heights);
        for(Pair<Integer, Integer> coordinate : pacSet){
            if(atlSet.contains(coordinate)){
                int first = coordinate.getKey();
                int second = coordinate.getValue();
                res.add(new ArrayList<>(Arrays.asList(first, second)));
            }
        }
        return res;
        
    }
    private void bfs(Queue<int[]> q, Set<Pair<Integer, Integer>> set, int[][] heights ){
        int[][] directions = {{1,0},{0,1},{-1,0},{0,-1}};
        while(!q.isEmpty()){
            int[] cell = q.poll();
            int r = cell[0];
            int c = cell[1];
            for(int[] dir : directions){
                int nr = r + dir[0];
                int nc = c + dir[1];
                Pair<Integer,Integer> next = new Pair<>(nr,nc);

                if(nr < 0 || nr >= rows || nc < 0 || nc >= cols){
                    continue;
                }
                if(!set.contains(next) && heights[r][c] <= heights[nr][nc]){
                    set.add(new Pair<>(nr,nc));
                    q.offer(new int[]{nr, nc});
                }
            }
        }
    }
}

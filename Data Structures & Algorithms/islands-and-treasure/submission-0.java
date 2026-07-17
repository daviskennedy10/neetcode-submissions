class Solution {
    int rows;
    int cols;
    public void islandsAndTreasure(int[][] grid) {
        Queue<int[]> q = new LinkedList<>();
        rows = grid.length;
        cols = grid[0].length;
        for(int i = 0; i < rows; i++){
            for(int j = 0; j < cols; j++){
                if(grid[i][j] == 0){
                    q.offer(new int[]{i,j});
                }
            }
        }
        if(q.size()== 0){
            return;
        }
        int[][] directions = {{0,-1},{-1,0},{1,0},{0,1}};
        while(!q.isEmpty()){
            int[] cell = q.poll();
            int r = cell[0];
            int c = cell[1];
            for(int[] dir : directions){
                int nr = r + dir[0];
                int nc = c + dir[1];
                if(nr >= rows || nr < 0 || nc >= cols || nc < 0 || grid[nr][nc] != Integer.MAX_VALUE ){
                    continue;
                }
                q.offer(new int[]{nr, nc});
                grid[nr][nc] = grid[r][c] + 1;
                
            }

        }
    }
    
}

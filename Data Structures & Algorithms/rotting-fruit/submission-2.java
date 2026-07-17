class Solution {
    public int orangesRotting(int[][] grid) {
        Queue<int[]> q = new LinkedList<>();
        int rows = grid.length;
        int cols = grid[0].length;
        int count = 0;
        int fresh = 0;

        for(int i = 0; i < rows; i++){
            for(int j = 0; j < cols; j++){
                if(grid[i][j] == 2){
                    q.offer(new int[]{i, j});
                }
                else if(grid[i][j] == 1){
                    fresh++;
                }
            }
        }
        if(fresh == 0){
            return 0;
        }
        int[][] directions = {{1,0},{0,1},{-1,0},{0,-1}};
        while(!q.isEmpty()){
            boolean didWeRot = false;
            int qLen = q.size();
            for(int z = 0; z < qLen; z++){
                int[] cell = q.poll();
                int r = cell[0];
                int c = cell[1];
                for(int[] dir : directions){
                    int nr = r + dir[0];
                    int nc = c + dir[1];
                    if(nr < 0 || nr >= rows || nc < 0 || nc >= cols){
                        continue;
                    }
                
                    if(grid[nr][nc] == 1){
                        grid[nr][nc] = 2;
                        didWeRot = true;
                        fresh--;
                        q.offer(new int[]{nr, nc});
                    }
                    
                }
                
            }
            if(didWeRot){
                count++;
            }
            
            
        }
        if(fresh > 0){
            return -1;
        }
        else{
            return count;
        }

    }
}

class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int res = 0;
        int max = 0;
        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j < grid[0].length; j++){
                if(grid[i][j] == 1){
                    res = dfs(i,j, grid);
                    max = Math.max(max, res);


                }
                

            }
        }
        return max;
    }
    private int dfs(int i, int j, int[][] grid){
        if(i < 0 || i >= grid.length || j < 0 || j >= grid[0].length || grid[i][j] == 0){
            return 0;
        }
        grid[i][j] = 0;
        int count = 1;
        count += dfs(i+1, j, grid);
        count += dfs(i-1, j, grid);
        count += dfs(i, j+1, grid);
        count += dfs(i, j-1, grid);
        return count;

        
    }
}

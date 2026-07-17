class Solution {
    boolean[][] visited;
    int rows;
    int cols;

    public boolean exist(char[][] board, String word) {
        rows = board.length;
        cols = board[0].length;
        visited = new boolean[rows][cols];

        for(int i = 0; i < rows; i++){
            for(int j = 0; j < cols; j++){
                if(dfs(board, word, i,j,0)){
                    return true;
                }
            }
        }
        return false;
    }
    private boolean dfs(char[][] board, String word, int r, int c, int k){
        if(r < 0 || c < 0 || r >= rows || c >= cols || board[r][c] != word.charAt(k) || visited[r][c] == true){
            return false;
        }
        if(k == word.length() - 1){
            return true;
        }
        visited[r][c] = true;
        boolean res = dfs(board, word, r+1, c, k+1) || dfs(board, word, r-1, c, k+1) || dfs(board, word, r, c+1, k+1) || dfs(board, word, r, c-1, k+1);
        visited[r][c] = false;
        return res;
    }
}

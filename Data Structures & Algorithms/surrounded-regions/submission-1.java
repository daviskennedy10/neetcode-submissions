class Solution {
    int rows;
    int cols;
    public void solve(char[][] board) {
        rows = board.length;
        cols = board[0].length;
        for(int i = 0; i < rows; i++){
            if(board[i][0] == 'O'){
                dfs(i, 0, board);
            }
            if(board[i][cols-1] =='O'){
                dfs(i, cols-1, board);
            }
        }
        for(int j = 0; j < cols; j++){
            if(board[0][j] == 'O'){
                dfs(0, j, board);
            }
            if(board[rows-1][j] =='O'){
                dfs(rows-1, j, board);
            }
        }
        for(int r = 0; r < rows; r++){
            for(int c = 0; c < cols; c++){
                if(board[r][c] == 'O'){
                    board[r][c] = 'X';
                }
                else if(board[r][c] == 'T'){
                    board[r][c] = 'O';
                }


            }
        }

    }
    private void dfs(int i, int j, char[][] board){
        if(i < 0 || i >= rows || j < 0 || j >= cols || board[i][j] != 'O'){
            return;
        }
        board[i][j] = 'T';
        dfs(i+1,j,board);
        dfs(i,j+1,board);
        dfs(i-1,j,board);
        dfs(i,j-1,board);
    }
}

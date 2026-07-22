class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        


        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != "O":
                return 

            if board[r][c] == "O":
                board[r][c] = "T"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or c == 0 or r == rows-1 or c == cols-1) and board[r][c] == "O":
                    dfs(r,c)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"
        
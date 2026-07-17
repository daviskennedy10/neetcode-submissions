class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        pos_diag = set()
        neg_diag = set()
        col = set()
        board = [["."] * n for i in range(n)]
        res = []

        def dfs(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col:
                    continue
                if r-c in neg_diag:
                    continue
                if r+c in pos_diag:
                    continue
                board[r][c] = "Q"
                col.add(c)
                neg_diag.add(r-c)
                pos_diag.add(r+c)
                dfs(r+1)
                col.remove(c)
                neg_diag.remove(r-c)
                pos_diag.remove(r+c)
                board[r][c] = "."
        
        dfs(0)
        return res
                
            

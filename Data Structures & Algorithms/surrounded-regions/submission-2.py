class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        q = deque()
        


        def canReach(r,c, visited):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return True

            if board[r][c] == "X" or (r,c) in visited:
                return False
            visited.add((r,c))
            if(canReach(r+1,c,visited) or canReach(r-1,c,visited) or canReach(r,c+1,visited) or canReach(r,c-1,visited)):
                return True
            return False
            
        for r in range(rows):
            for c in range(cols):
                
                if board[r][c] == "O":
                    q.append((r,c))
        
        while q:
            visited = set()
            value = q.popleft()
            r = value[0]
            c = value[1]
            if canReach(r,c,visited):
                board[r][c] = "T"
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"
        
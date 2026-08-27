class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        hold = matrix[0]
        rows = len(matrix)
        cols = len(matrix[0])
        idx = 0
        use = []
        for r in range(rows):
            for c in range(cols):
                use.append(matrix[r][c])
        
        for c in range(cols):
            for r in range(rows-1,-1,-1):
                matrix[r][c] = use.pop()


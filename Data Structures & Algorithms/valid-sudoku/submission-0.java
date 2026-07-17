class Solution {
    public boolean isValidSudoku(char[][] board) {
        Map<Integer, Set<Character>> rows = new HashMap<>();
        Map<Integer, Set<Character>> col = new HashMap<>();
        Map<String, Set<Character>> grid = new HashMap<>();
        for(int r = 0; r < board.length; r++){
            for(int c = 0; c < board[r].length; c++){
                if(board[r][c] == '.'){
                    continue;
                }
                String gridKey = (r /3) + "," + (c/3);

                if(rows.computeIfAbsent(r, k -> new HashSet<>() ).contains(board[r][c]) 
                || col.computeIfAbsent(c, k -> new HashSet<>() ).contains(board[r][c]) 
                || grid.computeIfAbsent(gridKey, k -> new HashSet<>() ).contains(board[r][c])){
                    return false;
                }
                rows.get(r).add(board[r][c]);
                col.get(c).add(board[r][c]);
                grid.get(gridKey).add(board[r][c]);


            }
        }
        return true;
    }
}      
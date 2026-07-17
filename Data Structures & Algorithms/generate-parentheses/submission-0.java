class Solution {
    List<String> res;
    public List<String> generateParenthesis(int n) {
        res = new ArrayList<>();
        dfs(n, "", 0,0);
        return res;
    }
    private void dfs(int n, String word, int open, int close){
        if(word.length() == 2*n){
            res.add(word);
            return;
        }
        if(close > open){
            return;
        }
        if(open < n){
            dfs(n, word+ "(", open+1, close);
        }
        if(close < open){
            dfs(n, word + ")", open, close+1);
        }

        

    }
}

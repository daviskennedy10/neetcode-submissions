class Solution {
    List<List<String>> res;
    StringBuilder check;
    public List<List<String>> partition(String s) {
        res = new ArrayList<>();
        List<String> subset = new ArrayList<>();
        dfs(s, subset, 0);
        return res;
    }
    private void dfs(String s, List<String> subset, int i){
        int n = s.length();
        if(i == n){
            res.add(new ArrayList<>(subset));
            return;
        }
        for(int end = i; end < n; end++){
            if(isPalindrome(s,i,end)){
                subset.add(s.substring(i, end+1));
                dfs(s, subset, end+1);
                subset.remove(subset.size()-1);
            }
        }


    }
    private boolean isPalindrome(String word, int r, int l){
        while(r <= l){
            if(word.charAt(r) != word.charAt(l)){
                return false;
            }
            r++;
            l--;
        }
        return true;
    }
}

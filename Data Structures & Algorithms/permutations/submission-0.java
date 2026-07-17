class Solution {
    List<List<Integer>> res;
    public List<List<Integer>> permute(int[] nums) {
        res = new ArrayList<>();
        List<Integer> subset = new ArrayList<>();
        boolean[] checker = new boolean[nums.length];
        dfs(nums, subset, checker);
        return res;
    }
    private void dfs(int[] candidates, List<Integer> subset, boolean[] checker){
        if(subset.size() == candidates.length){
            res.add(new ArrayList<>(subset));
            return;
        }
        for(int i = 0; i < candidates.length; i++){
            if(!checker[i]){
                checker[i] = true;
                subset.add(candidates[i]);
                dfs(candidates, subset, checker);
                subset.remove(subset.size()-1);
                checker[i] = false;
            }
        }
    }
}

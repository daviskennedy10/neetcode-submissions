class Solution {
    List<List<Integer>> res;
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        res = new ArrayList<>();
        Arrays.sort(candidates);
        if(candidates.length == 0){
            return res;
        }
        List<Integer> subset = new ArrayList<>();
        dfs(candidates, 0, target, subset);
        return res;
    }
    private void dfs(int[] candidates, int i, int target, List<Integer> subset){
        if(target == 0){
            res.add(new ArrayList<>(subset));
            return;
        }
        if(target < 0 || i >= candidates.length){
            return;
        }
        subset.add(candidates[i]);
        dfs(candidates, i+1, target - candidates[i], subset);
        subset.remove(subset.size() - 1);
        while(i + 1 < candidates.length && candidates[i] == candidates[i+1]){
            i++;
        }
        dfs(candidates, i+1, target, subset);
    }
}

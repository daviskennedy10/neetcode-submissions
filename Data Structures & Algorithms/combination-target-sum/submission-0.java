class Solution {
    List<List<Integer>> res;
    public List<List<Integer>> combinationSum(int[] nums, int target) {
        res = new ArrayList<>();
        if(nums.length == 0){
            return res;
        }
        List<Integer> subset = new ArrayList<>();
        dfs(nums, 0, subset, target);
        return res;
    }
    private void dfs(int[] nums, int i, List<Integer> subset, int target){
        if(target == 0){
            res.add(new ArrayList<>(subset));
            return;
        }
        
        if(target < 0 || i >= nums.length){
            return;
        }
        subset.add(nums[i]);
        dfs(nums, i, subset, target - nums[i]);
        subset.remove(subset.size()-1);
        dfs(nums, i+1, subset, target);

    }
}

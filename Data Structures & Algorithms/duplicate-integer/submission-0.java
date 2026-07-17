class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> checker = new HashSet<>();
        for(int i = 0; i < nums.length; i++){
            Boolean add = checker.add(nums[i]);
            if(!add){
                return true;

            }
        }
        return false;
    }
}
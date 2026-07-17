class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        int l = 0;
        int r = nums.length - 1;
        for(int i = 0; i < nums.length; i++){
            if(i > 0 && nums[i] == nums[i-1]){
                continue;
            }
            l = i+1;
            r = nums.length - 1;

            while(l < r){
            int target = nums[i] + nums[l] + nums[r];
            if(target < 0){
                l++; 
            }
            else if(target > 0){
                r--;
            }
            else{
                List<Integer> adder = new ArrayList<>();
                adder.add(nums[i]);
                adder.add(nums[l]);
                adder.add(nums[r]);
                res.add(adder);
                l++;
                while(nums[l] == nums[l-1] && l < r){
                   l++;
                }
            }
            

        }
        
        }
        return res;

    }
}

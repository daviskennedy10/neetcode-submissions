class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        LinkedList<List<Integer>> result = new LinkedList<>();
        Arrays.sort(nums);
        for(int i = 0; i < nums.length-2; i++){ 
            if(i > 0 && nums[i] == nums[i-1]){
                continue;
            }
            int left = i+1;
            int right = nums.length-1;
            while(left < right){
                if(nums[i] + nums[left] + nums[right] == 0){
                    LinkedList<Integer> placer = new LinkedList<>();
                    placer.add(nums[i]);
                    placer.add(nums[left]);
                    placer.add(nums[right]);
                    result.add(placer);
                    left++;
                    right--;

                    while(left < right && nums[left] == nums[left - 1]){
                        left++;
                    }
                    while(left < right && nums[right] == nums[right + 1]){
                        right--;
                    }
                }
                else if(nums[left] + nums[right] + nums[i] < 0){
                    left++;
                }
                else if(nums[left] + nums[right] + nums[i] > 0){
                    right--;
                }               

            }

        }
        return result;
    }
}

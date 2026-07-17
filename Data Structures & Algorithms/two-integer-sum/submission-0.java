class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> placer = new HashMap<>();
        int[] result = new int[2];
        for(int i = 0; i < nums.length; i++){
            int difference = target - nums[i];
            
            if(placer.containsKey(nums[i])){
                result[0] = placer.get(nums[i]);
                result[1] = i;
                return result;
            }
            placer.put(difference, i);
        }
        return result;
    }
}

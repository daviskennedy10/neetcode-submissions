class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int difference = 0;
        int[] res = new int[2];
        for(int i = 0; i < nums.length; i++){
            difference = target - nums[i];
            if(map.containsKey(difference)){
                res[1] = i;
                res[0] = map.get(difference);

            }
            map.put(nums[i], i);
        }
        return res;
    }
}

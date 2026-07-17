class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] pre = new int[nums.length];
        int[] suff = new int[nums.length];
        pre[0] = 1;
        suff[nums.length - 1] = 1;
        for(int i = 1; i < nums.length; i++){
            pre[i] = pre[i-1] * nums[i-1];
        }
        for(int j = nums.length -2; j >= 0; j--){
            suff[j] = suff[j+1] * nums[j+1];
        }
        for(int z = 0; z < nums.length; z++){
            nums[z] = pre[z] * suff[z];
        }
        return nums;

    }
}

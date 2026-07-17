class Solution {
    public int findDuplicate(int[] nums) {
        int slow = 0;
        int fast = 0;
        while(true){
            slow = nums[slow];
            fast = nums[nums[fast]];
            if(slow == fast){
                break;
            }
        }
        int slowB = 0;
        while(true){
            slowB = nums[slowB];
            slow = nums[slow];
            if(slow == slowB){
                return slow;
            }
        }
    }
}

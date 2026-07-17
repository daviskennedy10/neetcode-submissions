class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> container = new HashSet<>();
        int longest = 0;
        int length = 0;
        for(int i = 0; i < nums.length; i++){
            container.add(nums[i]);
        }
        for(int i = 0; i < nums.length; i++){
            if(!container.contains(nums[i] - 1)){
                length = 1;
                while(container.contains(nums[i] + length)){
                    length++;
                }
                longest = Math.max(longest, length);

            }
        }
        return longest;

    }
}

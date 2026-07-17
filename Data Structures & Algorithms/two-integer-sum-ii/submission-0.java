class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int right = numbers.length-1;
        int left = 0;
        int[] res = new int[2];
        while(left < right){
            if(numbers[right] + numbers[left] == target){
                res[0] = left+1;
                res[1] = right+1;
                break;
            }
            else if(numbers[right] + numbers[left] < target){
                left++;
            }
            else{
                right--;
            }
        }
        return res;
    }
}

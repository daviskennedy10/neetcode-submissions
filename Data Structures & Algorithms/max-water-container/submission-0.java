class Solution {
    public int maxArea(int[] heights) {
        int maximum = 0;
        int left = 0;
        int right = heights.length-1;
        while(left < right){
            int calc = Math.min(heights[left], heights[right]);
            int difference = right - left;
            int ans = calc * difference;
            maximum = Math.max(maximum, ans);
            if(heights[left] < heights[right]){
                left++;
            }
            else if(heights[left] == heights[right]){
                left++;
                right--;
            }
            else{
                right--;
            }

        }
        return maximum;
    }
}

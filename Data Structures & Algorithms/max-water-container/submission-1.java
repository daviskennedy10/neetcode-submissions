class Solution {
    public int maxArea(int[] heights) {
        int l = 0;
        int r = heights.length -1;
        int maximum = 0;
        int area = 0;
        while(l < r){
            int distance = r - l;
            int difference = Math.max(heights[l], heights[r]) - Math.min(heights[l], heights[r]);;
            int number = Math.min(heights[l], heights[r]);
            area = number * distance;
            maximum = Math.max(area, maximum);

            if(heights[l] <= heights[r]){
                l++;
            }
            else{
                r--;
            }
        }
        return maximum;
        
    }
}

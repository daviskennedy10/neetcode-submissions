class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0] * len(height)
        max_right = [0] * len(height)
        min_water = [0] * len(height)
        max_left[0] = height[0]
        max_right[len(height)-1] =  height[len(height)-1]

        for i in range(1, len(height)):
            max_left[i] = max(max_left[i-1], height[i])

        
        for b in range(len(height)-2, -1, -1):
            max_right[b] = max(max_right[b+1], height[b])
        
        for c in range(len(height)):
            min_water[c] = min(max_right[c], max_left[c])

        res = [0] * len(height)
        count = 0
        for a in range(len(height)):
            ans = min_water[a] - height[a]
            if ans < 0:
                res[a] = 0
            else: 
                res[a] = ans
            count += res[a]

        return count
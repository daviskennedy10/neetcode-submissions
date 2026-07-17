class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        next_small = [n] * n
        prev_small = [-1] * n
        stack = []
        area = 0
        res = 0
        
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                use = stack.pop()
                next_small[use] = i
            if stack:
                prev_small[i] = stack[-1]
            stack.append(i)
        
        for j in range(n):
            width = next_small[j] - prev_small[j] - 1
            height = heights[j]
            area = width * height
            res = max(area, res)
        return res
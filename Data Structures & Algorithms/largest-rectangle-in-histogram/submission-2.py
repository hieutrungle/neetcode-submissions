class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        left_bounds = [-1] * n
        left_stack = []
        for i, h in enumerate(heights):
            while left_stack and heights[left_stack[-1]] >= h:
                left_stack.pop()
            if left_stack:
                left_bounds[i] = left_stack[-1]
            left_stack.append(i)

        
        right_bounds = [n] * n
        right_stack = []
        for i in range(n - 1, -1, -1):
            while right_stack and heights[right_stack[-1]] >= heights[i]:
                right_stack.pop()
            if right_stack:
                right_bounds[i] = right_stack[-1]
            right_stack.append(i)
        
        res = 0
        for i in range(n):
            width = right_bounds[i] - left_bounds[i] - 1
            res = max(res, width * heights[i])

        return res
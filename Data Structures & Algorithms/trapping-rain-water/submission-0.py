class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_left, max_right = height[l], height[r]
        res = 0
        while l < r:
            if height[l] < height[r]:
                max_left = max(max_left, height[l])
                res += max_left - height[l]
                l += 1
            else:
                max_right = max(max_right, height[r])
                res += max_right - height[r]
                r -= 1
        return res
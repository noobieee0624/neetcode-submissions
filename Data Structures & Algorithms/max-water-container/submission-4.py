class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        max_v = 0

        while l < r:
            h = 0
            if heights[r] < heights[l]:
                h = heights[r]
            else:
                h = heights[l]
            
            max_v = max(h*(r-l), max_v)

            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        return max_v
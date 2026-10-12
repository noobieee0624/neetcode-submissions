class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        max_v = 0
        while l<r:
            width = r-l
            height = heights[l]
            if heights[l] > heights[r]:
                height = heights[r]
            else:
                height = heights[l]
            
            curr_v = height * width
            max_v = max(curr_v, max_v)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return max_v


        
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        ideation: we have left and right pointer, increment the pointer that
        is shorter, since the amount of water that we can hold is determined
        by the shroter pillar. In case of a tie, move either pointer, since
        even if we discover a taller pillar, we are constrained to the 
        shorter one
        '''
        l, r = 0, len(heights)-1
        max_volume = 0

        while l < r:
            height = min(heights[l], heights[r])
            width = r-l
            
            max_volume = max(height*width, max_volume)

            if heights[l] > heights[r]:
                r -= 1
            elif heights[l] <= heights[r]:
                l += 1
            
        return max_volume

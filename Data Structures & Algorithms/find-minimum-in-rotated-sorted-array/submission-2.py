class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        Two pointers: l, r

        if l < r, then that means array is already sorted, so return l

        otherwise, l must be > r, so we move l until next number is less than
        the current value of l, since list is originally sorted
        '''
        l, r = 0, len(nums)-1

        # as long as l and r don't intersect, we keep searching
        while l < r:
            if nums[l] < nums[r]:
                return nums[l]
            
            l += 1
        
        return nums[l]
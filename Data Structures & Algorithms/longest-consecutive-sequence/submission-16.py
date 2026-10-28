class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        we define the number as the start of a sequence if there's no
        immediate number smaller than the number we are looking at
        '''

        numset = set(nums)
        longest = 0

        for num in numset:
            length = 1

            #if we are looking at the start of the sequece
            if num-1 not in numset: 
                while num+length in numset:
                    length += 1
            longest = max(length, longest)
        
        return longest

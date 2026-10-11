class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # remove all duplicates from the set
        num_set = set(nums)
        max_count = 0

        for num in num_set:
            # we can define num as a starting number if num-1 isnt in the list 
            # then keep iterating until num+curr is no longer in the set, where curr is 
            # the current number of consecutive numbers
            if num-1 not in num_set:
                curr = 1
                while num+curr in num_set:
                    curr += 1
                max_count = max(curr, max_count)
        return max_count
                


        

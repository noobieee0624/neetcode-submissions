class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        count = 1
        longest = 0

        for num in nums:
            if num-1 not in num_set:
                while num+count in num_set:
                    count += 1
                longest = max(count, longest)
            count = 1
        return longest
                    
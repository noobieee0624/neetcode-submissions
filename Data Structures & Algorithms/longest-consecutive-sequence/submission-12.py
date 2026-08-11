class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        count = 1

        for num in numSet:
            if (num - 1) not in numSet:
                while (num + count) in numSet:
                    count += 1
                longest = max(count, longest)
            count = 1
        return longest
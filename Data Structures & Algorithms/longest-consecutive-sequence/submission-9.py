class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 1
        longest = 0
        numset = set(nums)

        for num in numset:
            if (num - 1) not in numset:
                while (num + count) in numset:
                    count += 1
                longest = max(count, longest)
            count = 1
        return longest

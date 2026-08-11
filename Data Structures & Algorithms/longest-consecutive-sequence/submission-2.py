class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 1
        curr = 1
        seen = set()
        starts = set()

        # filter list into a set for constant time look ups
        for num in nums:
            if num not in seen:
                seen.add(num)
        
        if not seen:
            return 0
        
        # find all starting numbers of sequences
        for num in seen:
            if num -1 in seen:
                continue
            elif num -1 not in seen and num + 1 in seen:
                starts.add(num)
        
        # find the longest sequence usign the list of starts
        if not starts:
            return count
        for start in starts:
            curr += 1
            while start + curr in seen:
                curr += 1
            if curr > count:
                count = curr
            curr = 0
        
        return count

        
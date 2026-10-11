class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        length = 0
        # maps a value in the window to the index where it was last seen
        seen = {}
        
        for i in range(0, len(s), +1):
            r = i
            if s[r] not in seen:
                seen[s[r]] = i
            else:
                l = max(l, seen[s[r]]+1)
                seen[s[r]] = r
            length = max(length, r-l+1)
        return length

        

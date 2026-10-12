class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        seen = {}
        length = 0

        for i, char in enumerate(s):
            if char not in seen:
                seen[char] = i
            elif char in seen and l <= seen[char]:
                l = seen[char]+1
            length = max(r-l+1, length)
            r += 1
            seen[char] = i
        
        return length
        

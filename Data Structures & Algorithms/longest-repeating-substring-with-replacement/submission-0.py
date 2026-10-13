class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_curr = 0
        l = 0
        in_window = {}
        res = 0

        for r in range(len(s)):
            in_window[s[r]] = in_window.get(s[r], 0) + 1
            max_curr = max(max_curr, in_window[s[r]])

            while (r-l+1)-max_curr > k:
                in_window[s[l]] -= 1
                l += 1
            
            res = max(res, r-l+1)
        
        return res



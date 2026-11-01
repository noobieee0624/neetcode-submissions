class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # keep track of the frequency of each letter in our window
        in_window = {}
        l = 0
        max_curr = 0
        longest = 0

        for r in range(len(s)):
            # we just increased our window from the right to add this letter
            # adjust accordingly into our dictionary
            in_window[s[r]] = in_window.get(s[r], 0) + 1
            # if s[r] has more frequencies than the current max frequency
            # in the window, we need to update max_curr
            max_curr = max(max_curr, in_window[s[r]])

            # since we added another char into our window by incrementing
            # the for loop, we need to readjust the left pointer and
            # shrink our window from the left
            while (r-l+1)-max_curr > k:
                in_window[s[l]] -= 1
                l += 1
            
            # after shrinking our window, we can reasses our max length ever
            longest = max(longest, r-l+1)                
        
        return longest

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqs = {}
        freqt = {}

        for c in s:
            freqs[c] = freqs.get(c, 0) + 1
        
        for c in t:
            freqt[c] = freqt.get(c, 0) + 1

        return freqs == freqt
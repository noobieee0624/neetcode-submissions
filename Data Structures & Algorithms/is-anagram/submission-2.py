class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hold the count of each character in s1 and s2
        # equate the two dictionaries at the end
        chars_1 = {}
        chars_2 = {}

        for char in s:
            chars_1[char] = chars_1.get(char, 0) + 1

        for char in t:
            chars_2[char] = chars_2.get(char, 0 ) + 1
        
        return chars_1 == chars_2

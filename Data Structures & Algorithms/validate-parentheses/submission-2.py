class Solution:
    def isValid(self, s: str) -> bool:
        first_half = ""
        key = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        stack = []
        length = len(s)

        if length%2 != 0:
            return False

        for char in s:
            if char in key:
                stack.append(key[char])
            elif not stack:
                return False
            else:
                if char != stack.pop():
                    return False

        if stack:
            return False
            
        return True
            




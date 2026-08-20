class Solution:
    def isValid(self, s: str) -> bool:
        first_half = ""
        key = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        stack = []

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
            




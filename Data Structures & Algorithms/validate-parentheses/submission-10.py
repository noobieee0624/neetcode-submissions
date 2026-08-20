class Solution:
    def isValid(self, s: str) -> bool:
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

        return not stack
            




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
            elif not stack or stack[-1] != char:
                return False
            else:
                stack.pop()
        
        return not stack
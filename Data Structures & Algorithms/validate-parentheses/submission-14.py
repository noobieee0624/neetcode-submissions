class Solution:
    def isValid(self, s: str) -> bool:
        '''
        create a key for the paren to match with

        use a heap structure while we loop through the string, so that if we 
        get the closing paren, we can compare it to a stack of them, and
        they should be equal--> then we pop from the stack

        ex: "([{}])"
        stack:
        bottom )]} top

        we use a last in first out structure
        '''

        # a dictionary that maps an open paren to its closing
        opens = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        # a stack that will store the sequence the parens need to 
        # be closed in
        key = []

        # loop through the string
        for c in s:
            if c in opens:
                key.append(opens[c])
                continue
            elif not key or c != key.pop():
                return False
        
        if key:
            return False
            
        return True





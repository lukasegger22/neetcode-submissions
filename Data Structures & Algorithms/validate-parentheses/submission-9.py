class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {'(':')', '[':']' , '{': '}'}
        stack = []
        for bracket in s:
            if bracket in lookup:
                stack.append(bracket)
            else:
                if not stack:
                    return False
                brack = stack.pop()
                if lookup[brack] != bracket:
                    return False
                
        return True if not stack else False
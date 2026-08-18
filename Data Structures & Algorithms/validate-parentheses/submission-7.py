class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 ==1:
            return False
        lookup = {'(' : ')', '{' : '}', '[': ']'}
        stack = []
        for char in s:
            if char in lookup:
                stack.append(char)
            else:
                if not stack:
                    return False
                bracket = stack.pop()
                if lookup[bracket] != char:
                    return False
        return True if not stack else False


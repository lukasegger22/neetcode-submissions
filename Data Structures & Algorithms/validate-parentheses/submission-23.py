class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {'(':')', '{':'}', '[':']'}
        for char in s:
            if char in lookup:
                stack.append(char)
            else:
                if not stack:
                    return False
                elif lookup[stack[-1]] == char:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
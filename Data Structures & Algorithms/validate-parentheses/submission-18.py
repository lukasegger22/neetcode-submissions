class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        stack = []
        lookup = {'(' : ')','{' : '}', '[' : ']'}
        for char in s:
            if char in lookup:
                stack.append(char)
            else:
                if stack:
                    last_char = stack.pop()
                    print(last_char)
                    if char != lookup[last_char]:
                        return False
                else:
                    return False
        return True if not stack else False
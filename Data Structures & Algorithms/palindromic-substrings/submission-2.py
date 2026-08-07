class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i, char in enumerate(s):
            for j in range(2):
                left = i
                right = i + j
                while left >= 0 and right <= len(s)-1:
                    if s[left] == s[right]:
                        count+=1
                        left-=1
                        right+=1
                    else:
                        break
        return count

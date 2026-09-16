class Solution:
    def countSubstrings(self, s: str) -> int:
        def trypalindrom(left, right):
            tmp = 0
            while left >= 0 and right <= len(s)-1 and s[left] == s[right]:
                left-=1
                right+=1
                tmp+=1
            return tmp
        count = 0
        for i in range(len(s)):
            even_pal = trypalindrom(i,i)
            odd_pal = trypalindrom(i,i+1)
            count += even_pal + odd_pal
        return count
class Solution:
    def countSubstrings(self, s: str) -> int:
        def trypalindrom(left, right,tmp):
            tmp = 0
            while left >= 0 and right <= len(s)-1 and s[left] == s[right]:
                left-=1
                right+=1
                tmp+=1
            return tmp
        result = []
        count = 0
        for i, char in enumerate(s):
            even_pal = trypalindrom(i,i,count)
            odd_pal = trypalindrom(i,i+1,count)
            count = count + even_pal + odd_pal
        return count
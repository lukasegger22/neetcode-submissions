class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        count_t = {}
        for char in t:
            count_t[char]=count_t.get(char,0)+1
        left = 0
        count_s = {}
        min_value = float('inf')
        need = len(count_t)
        have = 0
        best_l = 0
        best_r = 0
        for right in range(len(s)):
            char = s[right]
            count_s[char] = count_s.get(char,0)+1
            if char in count_t and count_s[char] == count_t[char]:
                have+=1
                while left<=right and have == need:
                    if min_value > right-left+1:
                        best_l = left
                        best_r = right
                        min_value = min(min_value, right-left+1)
                    count_s[s[left]]-=1
                    if s[left] in count_t and count_s[s[left]] < count_t[s[left]]:
                        have-=1
                    if count_s[s[left]] == 0:
                        del count_s[s[left]]
                    left+=1
        return s[best_l:best_r+1] if min_value != float('inf') else ""


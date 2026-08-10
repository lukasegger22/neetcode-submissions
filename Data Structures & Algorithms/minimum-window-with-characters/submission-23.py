class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        count_t = {}
        for char in t:
            count_t[char] = count_t.get(char,0)+1
        count_s = {}
        best_l = 0
        best_r = 0
        min_length = float("inf")
        need = len(count_t)
        have = 0
        left = 0
        for i, char in enumerate(s):
            count_s[char] = count_s.get(char,0)+1
            if char in count_t and count_t[char] == count_s[char]:
                have+=1
                while have == need:
                    if min_length > (i-left+1):
                        min_length = i-left+1
                        best_l = left
                        best_r = i
                    if s[left] in count_t and count_s[s[left]] == count_t[s[left]]:
                        have-=1
                    count_s[s[left]]-=1
                    if count_s[s[left]] == 0:
                        del count_s[s[left]]
                    
                    left+=1
        print(min_length)
        return s[best_l:best_r+1] if min_length != float("inf") else ""

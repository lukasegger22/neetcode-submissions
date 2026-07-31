class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        count1 = {}
        for char in t:
            count1[char] = count1.get(char,0)+1
        left = 0
        best_l = 0
        best_r = 0
        have = 0
        need = len(count1)
        min_length = float("inf")
        count2 = {}
        for right in range(len(s)):
            count2[s[right]] = count2.get(s[right],0)+1
            if s[right] in count1 and count2[s[right]] == count1[s[right]]:
                have+=1
            while left <= right and have == need:
                if min_length >= right-left+1:
                    min_length = min(min_length , right-left+1)
                    best_l = left
                    best_r = right
                if s[left] in count1 and count2[s[left]] <= count1[s[left]]:
                    have-=1
                count2[s[left]]-=1
                if count2[s[left]] == 0:
                    del count2[s[left]]
                left+=1
        return s[best_l:best_r+1] if  min_length != float('inf') else ""

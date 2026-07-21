class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        count1 = {}
        for char in t:
            count1[char] = count1.get(char, 0)+1
        count2 = {}
        need = len(count1)
        left = 0
        min_range = float('inf')
        best_left = 0
        best_right = 0
        have = 0
        for right in range(len(s)):
            count2[s[right]]=count2.get(s[right],0)+1
            if s[right] in count1 and count2[s[right]] == count1[s[right]]:
                have+=1
            while have == need:
                if min_range > right-left+1:
                    min_range = right-left+1
                    best_left = left
                    best_right = right
                if s[left] in count1 and count2[s[left]] == count1[s[left]]:
                    have -= 1
                count2[s[left]]-=1
                if count2[s[left]] == 0:
                    del count2[s[left]]

                left+=1
        return "" if min_range == float('inf') else s[best_left:best_right+1]            


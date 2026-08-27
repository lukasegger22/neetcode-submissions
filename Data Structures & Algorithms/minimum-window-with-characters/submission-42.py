class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        count1 = {}
        for char in t:
            count1[char] = count1.get(char,0)+1
        left = 0
        right = 0
        count2 = {}
        have = 0
        need = len(count1)
        shortest_streak = float("inf")
        best_left = 0
        while right <= len(s)-1:
            count2[s[right]] = count2.get(s[right],0)+1
            if s[right] in count1 and count2[s[right]] == count1[s[right]]:
                have+=1
                while need == have:
                    if shortest_streak > right-left+1:
                        shortest_streak = right-left+1
                        best_left = left
                    if s[left] in count1 and count1[s[left]] == count2[s[left]]:
                        have-=1
                    count2[s[left]]-=1
                    if count2[s[left]] == 0:
                        del count2[s[left]]
                    left+=1
            right+=1
        return "" if shortest_streak == float("inf") else s[best_left:best_left+shortest_streak]


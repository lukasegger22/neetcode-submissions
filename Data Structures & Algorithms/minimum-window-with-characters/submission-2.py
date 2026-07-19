class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count1 = {}
        count2 = {}
        for char in t:
            count1[char] = count1.get(char, 0)+1
        need = len(count1)
        have = 0
        smallest_streak = float("inf")
        left = 0
        best_left = 0
        best_right = 0
        for right in range(len(s)):
            char = s[right]
            count2[char]= count2.get(char, 0)+1
            if char in count1 and count2[char] == count1[char]:
                have +=1
            if have == need:
                while s[left] not in count1 or count2[s[left]]-1 >= count1[s[left]]:
                    count2[s[left]]-=1
                    if count2[s[left]] == 0:
                        del count2[s[left]]
                    left+=1
                if smallest_streak > right-left+1:
                    smallest_streak = min(right-left+1,smallest_streak)
                    best_left = left
                    best_right = right
        return s[best_left:best_right+1] if smallest_streak != float("inf") else ""
                    
        



class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        longest_streak = 0
        for i, char in enumerate(s):
            count[char] = count.get(char,0)+1
            while (i-left+1) - max(count.values()) > k:
                count[s[left]]-=1
                if count[s[left]] == 0:
                    del count[s[left]]
                left+=1
            current_streak = i-left+1
            longest_streak = max(longest_streak, current_streak)
        return longest_streak

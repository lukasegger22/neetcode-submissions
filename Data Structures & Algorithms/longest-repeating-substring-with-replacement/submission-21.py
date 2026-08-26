class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        right = 0
        longest_streak = 0
        while right <= len(s)-1:
            count[s[right]] = count.get(s[right],0)+1
            while (right-left+1) - max(count.values()) > k:
                count[s[left]] -=1
                if count[s[left]] == 0:
                    del count[s[left]]
                left+=1
            longest_streak = max(longest_streak, right-left+1)
            right+=1
        return longest_streak

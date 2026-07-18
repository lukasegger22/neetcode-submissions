class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left= 0
        count = {}
        longest_streak = 0
        for right in range(len(s)):
            char = s[right]
            count[char] = count.get(char, 0) + 1
            while (right - left + 1) - max(count.values()) > k:
                count[s[left]]-=1
                left+=1
            longest_streak=max(longest_streak, right-left+1)
        return longest_streak


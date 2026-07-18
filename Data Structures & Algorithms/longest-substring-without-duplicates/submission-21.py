class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        longest_streak = 0
        left= 0
        for right in range(len(s)):
            char = s[right]
            while char in unique:
                unique.remove(s[left])
                left+=1
            unique.add(char)
            longest_streak = max(longest_streak, right-left+1)
        return longest_streak
        
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        left = 0
        max_length = 0
        for right in range(len(s)):
            char = s[right]
            while char in unique:
                unique.remove(s[left])
                left+=1
            unique.add(char)
            max_length = max(max_length, right-left +1)
        return max_length
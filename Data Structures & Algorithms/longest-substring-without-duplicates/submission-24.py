class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        count = set()
        longest_streak = 0
        for right in range(len(s)):
            char = s[right]
            
            while char in count: 
                count.remove(s[left])
                left+=1
            count.add(char)
            longest_streak = max(right-left+1, longest_streak)
        return longest_streak


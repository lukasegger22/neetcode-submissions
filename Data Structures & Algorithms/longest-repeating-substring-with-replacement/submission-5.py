class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}
        longest_streak = 0
        for right in range(len(s)):
            char = s[right]
            count[char] = count.get(char,0)+1
            max_value = max(count.values())
            while (right-left) - max_value >= k and left < right:
                count[s[left]]-=1
                left+=1
                max_value = max(count.values())
            longest_streak = max(right-left+1, longest_streak)
        return longest_streak
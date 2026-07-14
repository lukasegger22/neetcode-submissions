class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right= 0
        count = defaultdict(list)
        longest_streak = 0
        current_streak = 0
        for right in range(len(s)):
            char = s[right]
            if char not in count:
                count[char] = 1
            else: 
                count[char]+=1
            max_values =max(count.values())
            if (right-left+1) - max_values <= k:
                current_streak += 1
                if longest_streak <current_streak:
                    longest_streak = current_streak
                right+=1
            else:
                count[s[left]]-=1
                left+=1

        return longest_streak


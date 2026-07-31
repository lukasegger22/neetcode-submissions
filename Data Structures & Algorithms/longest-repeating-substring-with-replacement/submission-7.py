class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}
        max_length = float("-inf")
        max_val = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right],0)+1
            max_val = max(max_val, count[s[right]])
            while right-left+1 - max_val > k:
                count[s[left]]-=1
                if count[s[left]] == 0:
                    del count[s[left]]
                left+=1
            if max_length < right-left+1:
                    max_length = right-left+1
        return max_length



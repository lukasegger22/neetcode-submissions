class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        count = {}
        longest_seq = 0
        while right <= len(s)-1:
            while s[right] in count:
                count[s[left]] -=1
                if count[s[left]] == 0:
                    del count[s[left]]
                left+=1
            count[s[right]] = count.get(s[right], 0) + 1
            longest_seq = max(longest_seq, len(count))
            right+=1
        return longest_seq
                

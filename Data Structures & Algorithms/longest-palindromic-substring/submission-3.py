class Solution:
    def longestPalindrome(self, s: str) -> str:
        best_start = 0
        max_length = 0
        for i, char in enumerate(s):
            for j in range(2):
                left = i
                right = left + j
                current_start = i
                while left >= 0 and right <= len(s)-1:
                    if s[left] == s[right]:
                        current_start = left
                        if max_length < right-left+1:
                            max_length = right-left+1
                            best_start = current_start
                        left-=1
                        right+=1
                    else:
                        break
        return s[best_start:best_start+max_length]

                        
                    



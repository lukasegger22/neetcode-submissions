class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        biggest_length = 0
        longest_str = ""
        for i, char in enumerate(s):
            for j in range(2):
                left = i
                right = left + j
                best_l = 0
                best_r = 0
                while left >= 0 and right < len(s):
                    if s[left] == s[right] :
                        best_l = left
                        best_r = right
                        if best_r - best_l + 1 > biggest_length:
                            biggest_length = best_r - best_l + 1
                            longest_str = s[best_l: best_r+1]
                        left-=1
                        right+=1
                    else:
                        break
        return longest_str
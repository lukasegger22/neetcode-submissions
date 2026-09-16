class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_from_center(left: int, right: int):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - left - 1
        
        max_start = 0
        max_length = 0
        
        for i in range(len(s)):
            start_odd, len_odd = expand_from_center(i, i)
            start_even, len_even = expand_from_center(i, i + 1)
            
            if len_odd > max_length:
                max_length = len_odd
                max_start = start_odd
                
            if len_even > max_length:
                max_length = len_even
                max_start = start_even
                
        return s[max_start : max_start + max_length]
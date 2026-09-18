class Solution:
    def longestPalindrome(self, s: str) -> str:
        def trypalindrom(left, right):
            count = 0
            while left >= 0 and right <= len(s)-1 and s[left] == s[right]:
                left-=1
                right+=1
            return (right - left - 1), (left + 1)
        max_length = 0
        max_left = 0
        for i, char in enumerate(s):
            current_length = 0
            current_left = 0
            for shift in range(2):
                laenge, start = trypalindrom(i, i+shift)
                if laenge > current_length:
                    current_length = laenge
                    current_left = start
            if current_length > max_length:
                max_length = current_length
                max_left = current_left
        return s[max_left : max_left + max_length]

            

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        one_step_ways = 1
        two_step_ways = 1
        for i in range(1, len(s)):
            current_ways = 0
            if int(s[i]) != 0:
                current_ways += one_step_ways
            if int(s[i-1:i+1]) >= 10 and int(s[i-1:i+1]) <= 26:
                current_ways += two_step_ways
            two_step_ways, one_step_ways = one_step_ways, current_ways
        return one_step_ways

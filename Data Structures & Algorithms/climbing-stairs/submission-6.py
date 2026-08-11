class Solution:
    def climbStairs(self, n: int) -> int:
        if n<= 3:
            return n
        one_step = 1
        two_step = 1
        for i in range(n):
            two_step, one_step = one_step, one_step + two_step
        return two_step
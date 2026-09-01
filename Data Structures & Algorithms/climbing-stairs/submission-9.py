class Solution:
    def climbStairs(self, n: int) -> int:
        one_step = 0
        two_step = 1
        for i in range(n):
            one_step , two_step = two_step, one_step + two_step
        return two_step

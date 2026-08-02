class Solution:
    def climbStairs(self, n: int) -> int:
        i = 2
        one_step = 2
        two_steps = 1
        tmp = 0
        if n ==1:
            return 1
        elif n == 2:
            return one_step
        elif n == 3:
            return one_step+two_steps
        while i+1 < n:
            tmp = one_step+two_steps
            two_steps = one_step
            one_step = tmp
            i+=1
        return one_step+two_steps


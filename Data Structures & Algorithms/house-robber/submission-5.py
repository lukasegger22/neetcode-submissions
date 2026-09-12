class Solution:
    def rob(self, nums: List[int]) -> int:
        one_step = 0
        two_step = 0
        for n in nums:
            max_rob = max(n+two_step, one_step)
            print(max_rob)
            two_step, one_step = one_step, max_rob
        return max(two_step, one_step)

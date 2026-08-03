class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def helper(houses):
            rob1 = 0
            rob2 = 0
            for n in houses:
                current_max = max(n + rob1, rob2)
                rob1, rob2 = rob2, current_max
            return rob2
        return max(helper(nums[1:]), helper(nums[:-1]))
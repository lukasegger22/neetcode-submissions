class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = 0
        rob2 = 0
        for n in nums:
            current_max = max(rob1+n, rob2)
            rob2, rob1 = current_max , rob2
        return rob2
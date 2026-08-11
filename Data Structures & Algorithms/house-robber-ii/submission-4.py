class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        rob1 = 0
        rob2 = 0
        for n in nums[1:]:
            current_max = max(rob1+n, rob2)
            rob1, rob2 = rob2 , current_max
        current1 = rob2
        rob1 = 0
        rob2 = 0
        for n in nums[:len(nums)-1]:
            current_max = max(rob1+n, rob2)
            rob1, rob2 = rob2 , current_max
        current2 = rob2 
        return max(current1, current2)
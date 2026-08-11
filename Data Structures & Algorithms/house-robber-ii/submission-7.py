class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        def helper_houses(nums):
            rob1 = 0
            rob2 = 0
            for n in nums:
                current_max = max(rob1+n, rob2)
                rob1, rob2 = rob2 , current_max
            return rob2
            
        return max(helper_houses(nums[1:]), helper_houses(nums[:len(nums)-1]))
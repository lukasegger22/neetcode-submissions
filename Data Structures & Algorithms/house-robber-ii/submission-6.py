class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        max_result = 0
        numbers = [nums[1:], nums[:len(nums)-1]]
        for number in numbers:
            rob1 = 0
            rob2 = 0
            for n in number:
                current_max = max(rob1+n, rob2)
                rob1, rob2 = rob2 , current_max
            current1 = rob2
            max_result = max(max_result, current1)
        return max_result
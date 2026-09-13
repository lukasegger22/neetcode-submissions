class Solution:
    def rob(self, nums: List[int]) -> int:
        def RobWithLength(nums):
            one_step = 0
            two_step = 0
            for n in nums:
                max_rob = max(n+two_step, one_step)
                two_step, one_step = one_step, max_rob
            return max(one_step, two_step)
        nums1 = RobWithLength(nums[1:])
        nums2 = RobWithLength(nums[:-1])
        return max(nums1,nums2) if len(nums)>1 else nums[0]



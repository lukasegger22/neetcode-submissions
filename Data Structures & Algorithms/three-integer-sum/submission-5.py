class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        for index, number in enumerate(nums):
            left = index+1
            right = len(nums)-1
            if index > 0 and nums[index] == nums[index-1]:
                continue
            while left < right:
                current_sum = number + nums[left] + nums[right]
                if current_sum == 0:
                    result.append([nums[left], number, nums[right]])
                    left+=1
                    right-=1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif current_sum > 0:
                    right-=1
                elif current_sum < 0:
                    left+=1
        return result
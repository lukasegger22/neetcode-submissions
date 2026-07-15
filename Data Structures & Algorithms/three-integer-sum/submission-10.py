class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for index, number in enumerate(nums):
            if index > 0 and number == nums[index - 1]:
                continue
            left = index+1
            right=len(nums)-1
            while left < right:
                tmp = nums[left] + nums[right] + number
                if tmp == 0:
                    result.append([nums[left],number,nums[right]])
                    left+=1
                    right-=1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif tmp > 0:
                    right-=1
                else:
                    left+=1
        return result

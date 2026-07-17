class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for index, number in enumerate(nums):
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            left = index+1
            right = len(nums)-1
            while left < right:
                calc = nums[left] + number + nums[right]
                if calc == 0:
                    result.append([nums[left],number, nums[right]])
                    left+=1
                    right-=1
                    while left < right and nums[left-1] == nums[left]:
                        left+=1
                elif calc > 0:
                    right-=1
                else:
                    left+=1
        return result
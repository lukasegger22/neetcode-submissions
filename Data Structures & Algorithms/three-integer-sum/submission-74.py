class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i, number in enumerate(nums):
            if i > 0 and number == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            while left < right:
                tmp = number + nums[left] + nums[right]
                if tmp == 0:
                    result.append([number, nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left+=1
                    while left < right and nums[right] == nums[right-1]:
                        right-=1
                    right-=1
                    left+=1
                elif tmp > 0:
                    right-=1
                else:
                    left+=1
        return result
                
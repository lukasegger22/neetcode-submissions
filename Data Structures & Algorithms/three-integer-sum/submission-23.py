class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i, number in enumerate(nums):
            left = i + 1
            right = len(nums)-1
            if nums[i] == nums[i-1] and i > 0:
                continue
            while left < right:
                calc = number + nums[right] + nums[left]
                if calc == 0:
                    result.append([number,nums[right],nums[left]])
                    left+=1
                    right-=1
                    while nums[left] == nums[left-1] and left < right:
                        left+=1
                elif calc < 0:
                    left+=1
                else:
                    right-=1
        return result

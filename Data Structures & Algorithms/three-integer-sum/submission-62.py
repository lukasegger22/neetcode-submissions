class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i, number in enumerate(nums):
            left = i+1
            right = len(nums)-1
            if i > 0 and number == nums[i-1]:
                continue
            while left < right:
                calc = number + nums[left] + nums[right]
                if calc == 0:
                    result.append([number, nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left+=1
                    while left < right and nums[right] == nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
                elif calc > 0:
                    right-=1
                else:
                    left+=1
        return result




class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        tmp = 1
        for i in range(len(nums)-1):
            tmp *= nums[i]
            result[i+1] *= tmp
        tmp =1
        for i in range(len(nums)-1,-1,-1):
            result[i]*=tmp
            tmp*=nums[i]   
        return result
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left < right:
            mid = left + (right-left)//2
            if nums[left] == nums[right]:
                return nums[left]
            elif nums[left] <= nums[mid] <= nums[right]:
                if nums[left] <= nums[mid]:
                    right = mid
                else:
                    left = mid
            else:
                if nums[mid] > nums[right]:
                    left = mid+1
                else:
                    right = mid
        return nums[left]
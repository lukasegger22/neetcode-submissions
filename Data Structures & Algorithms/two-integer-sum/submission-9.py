class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        for i, number in enumerate(nums):
            calc = target - number
            if number in count:
                return [count[number], i]
            count[calc] = i
        return []
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        for i, number in enumerate(nums):
            tmp = target - number
            if tmp not in count:
                count[number]=i
            else:
                return [count[tmp], i ]
        return []
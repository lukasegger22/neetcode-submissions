class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        for i, number in enumerate(nums):
            tmp = target - number
            if tmp in count:
                return [count[tmp],i]
            count[number] = i
        return [0,0]
            

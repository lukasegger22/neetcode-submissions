class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = set()
        for number in nums:
            if number in count:
                return True
            count.add(number)
        return False
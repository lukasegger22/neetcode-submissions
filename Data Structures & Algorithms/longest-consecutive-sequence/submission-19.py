class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        longest_streak = 0
        for number in nums:
            if number-1 in numbers:
                continue
            else :
                count = 1
                while number+1 in numbers:
                    number+=1
                    count+=1
                longest_streak = max(count, longest_streak)
        return longest_streak

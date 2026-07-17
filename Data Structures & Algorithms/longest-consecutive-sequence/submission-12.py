class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        if len(nums) == 0:
            return 0
        longest_streak = 1
        for number in nums:
            if number-1 not in num_set:
                current_streak=1
                while number+1 in num_set:
                    number+=1
                    current_streak+=1
                    longest_streak = max(current_streak, longest_streak)
        return longest_streak

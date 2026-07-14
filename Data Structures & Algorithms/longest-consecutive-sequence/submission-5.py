class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        longest_streak=0
        if len(nums)==0:
            return 0
        for number in unique:
            if number-1 not in unique:
                current_num = number
                current_streak = 1
                while current_num+1 in unique:
                    current_num +=1
                    current_streak +=1
                if current_streak > longest_streak:
                    longest_streak = current_streak
        return longest_streak



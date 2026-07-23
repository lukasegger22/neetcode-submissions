class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        longest_streak = 0
        count = set()
        for number in nums:
            count.add(number)
        for number in count:
            current_streak = 1
            if not number-1 in count:
                while number+1 in count:
                    number+=1
                    current_streak+=1
                longest_streak = max(longest_streak, current_streak)
        return longest_streak


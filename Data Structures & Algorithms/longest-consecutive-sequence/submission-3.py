class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set()
        result=1
        if len(nums)==0:
            return 0
        for number in nums:
            unique.add(number)

            current_num = number
            current_streak = 1
            while current_num-1 in unique:
                current_num -=1
            while current_num+1 in unique:
                current_num +=1
                current_streak +=1
                if current_streak > result:
                    result = current_streak
        return result



class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                past_temp, past_index = stack.pop()
                wait_time = i - past_index
                result[past_index] = wait_time
            stack.append([temp,i])
        return result
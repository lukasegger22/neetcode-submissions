class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while len(stack) > 0 and stack[-1][1] < temp:
                val = stack.pop()
                result[val[0]] = i - val[0]
            stack.append((i,temp))
        return result

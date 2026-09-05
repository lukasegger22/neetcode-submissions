class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        current_area = 0
        for i, height in enumerate(heights):
            start_index = i
            while len(stack) > 0 and height < stack[-1][1]:
                val = stack.pop()
                start_index = val[0]
                current_area = val[1] * (i - val[0])
                max_area = max(max_area, current_area)
            stack.append((start_index, height))
        while len(stack) > 0:
            val = stack.pop()
            current_area = val[1] * (len(heights) - val[0])
            max_area = max(max_area, current_area)
        return max_area


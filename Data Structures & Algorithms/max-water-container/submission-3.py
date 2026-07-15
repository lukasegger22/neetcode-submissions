class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right=len(heights)-1
        biggest_vol = 0
        while left < right:
            current_vol = (right-left) * min(heights[left], heights[right])
            biggest_vol = max(biggest_vol, current_vol)
            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1
        return biggest_vol


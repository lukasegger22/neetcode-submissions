class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        min_rate = float("inf")
        while left <= right:
            mid = (left+right)//2
            count = 0
      
            for pile in piles:
                count+= (pile+mid-1)//mid
            if count <= h:
                right=mid-1
                min_rate = min(min_rate, mid)
            else:
                left=mid+1

        return min_rate


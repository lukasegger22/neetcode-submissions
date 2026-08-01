class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        min_pile = float("inf")
        while left <= right:
            mid = (right+left+1)//2
            current_length = 0
            for pile in piles:
                current_length += (pile  + mid - 1) // mid
            if current_length <= h:
                min_pile = min(min_pile, mid)
                right = mid-1
            else:
                left = mid+1
        return min_pile if min_pile != float("inf") else max(piles)
                
                
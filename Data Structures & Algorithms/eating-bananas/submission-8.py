class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        min_pile = right
        while left <= right:
            mid = (left+right)//2
            count = 0
            for i in range(len(piles)):
                count += (piles[i] + mid - 1) // mid
            if count > h:
                left = mid+1

            else:
                min_pile = mid
                right = mid - 1
        return min_pile
            
            

                

        

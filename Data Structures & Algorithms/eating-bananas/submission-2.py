class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        min_rate = float('inf')
        while left <= right:
            mid = (left + right) //2
            result = 0
            index = 0
            for index in range(len(piles)):
                result += math.ceil(piles[index]/mid)
                index+=1
            if result <= h:
                right = mid-1
                min_rate = min(min_rate, mid) 
            else:
                left= mid+1
            
        return min_rate


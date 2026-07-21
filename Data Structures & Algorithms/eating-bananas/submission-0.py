class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 0
        right = max(piles)
        min_rate = float('inf')
        while left <= right:
            mid = (left + right) //2
            result = 0
            index = 0
            while result <= h and index <= len(piles)-1:
                if mid ==0:
                    index+=1
                    continue
                result += math.ceil(piles[index]/mid)
                index+=1
            if result <= h and result !=0 :
                right = mid-1
                min_rate = min(min_rate, mid) 
            else:
                left= mid+1
            
        return min_rate


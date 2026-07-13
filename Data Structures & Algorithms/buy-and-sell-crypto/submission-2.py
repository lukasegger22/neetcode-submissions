class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        result = 0
        for price in prices:
            if price < minimum:
                minimum = price
            calc = price - minimum
            if calc  > result:
                result = calc 
        return result
        
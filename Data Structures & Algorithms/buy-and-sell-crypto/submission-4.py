class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value = prices[0]
        result = 0
        for price in prices:
            min_value = min(min_value, price)
            profit = price - min_value
            result = max(result, profit)
        return result

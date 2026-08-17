class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_val = 0
        for price in prices:
            min_price = min(min_price, price)
            current_max = price - min_price
            max_val = max(max_val, current_max)
        return max_val

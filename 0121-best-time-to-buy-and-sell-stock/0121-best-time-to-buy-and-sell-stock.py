class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        max_profit = float('-inf')
        for price in prices:
            sell = price
            profit = sell - buy
            max_profit = max(profit,max_profit)
            buy = min (buy,price)
        return max_profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = float('-inf')
        buy = prices[0]
        for i in range(len(prices)):
            maxProfit = max(maxProfit,prices[i]-buy)
            buy = min(buy,prices[i])
        return maxProfit
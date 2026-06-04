class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m, profit = prices[0], 0
        for d in range(len(prices)):
            if prices[d] < m:
                m = prices[d]
            if prices[d] - m > profit:
                profit = prices[d] - m
        return profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[r] <= prices[l]:
                l = r
            highest = max(highest, prices[r] - prices[l])
            r += 1
        return highest
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buyPrice = prices[0]
        for i, price in enumerate(prices[1:]):
            if price - buyPrice > 0:
                profit += price - buyPrice
                buyPrice = price
            else:
                buyPrice = price

        return profit
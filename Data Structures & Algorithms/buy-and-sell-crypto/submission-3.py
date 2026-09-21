class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # O(n)
        # Dynamic Programming 
        minBuy = prices[0]  # first price
        maxProfit = 0

        for sell in prices:     # consider selling on each day
            maxProfit = max(maxProfit, sell - minBuy)   # selling today - lowest buy price from earlier
            minBuy = min(minBuy, sell)      # finds day with smallest buy price
        return maxProfit
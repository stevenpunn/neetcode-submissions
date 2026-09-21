class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # keep track of the lowest price so far (day to buy)
        # track best profit (sell today minus lowest price seen before)
        maxProfit = 0
        minBuy = prices[0]

        # loop through each sell price
        for sell in prices:
            # update the maxProfit with sell price - buy price
            maxProfit = max(maxProfit, sell - minBuy)
            # update the minBuy price if we find a smaller price
            minBuy = min(minBuy, sell)
        return maxProfit
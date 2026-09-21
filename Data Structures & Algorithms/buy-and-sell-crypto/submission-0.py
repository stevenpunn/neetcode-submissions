class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0                                  # max profit
        for i in range(len(prices)):                # i = buy day
            buy = prices[i]                         # price for buying on day i
            for j in range(i+1, len(prices)):       # all future sell days
                sell = prices[j]                    # j = sell day
                result = max(result, sell-buy)      # return 0 if not, or sell-buy to find highest return
        return result
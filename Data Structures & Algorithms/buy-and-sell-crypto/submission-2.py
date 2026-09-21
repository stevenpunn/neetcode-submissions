class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # O(n)
        # 2 pointer approach
        l = 0
        r = 1
        maxProfit = 0

        # iterate r pointer until the end
        while r < len(prices):
            if prices[l] < prices[r]:       # while if sell > buy
                profit = prices[r] - prices[l] 
                maxProfit = max(maxProfit, profit)  # return highest
            else:   # if that was not profitable
                l = r     # new buy day replaces old selling day (found the cheapest buy day)
            r += 1        # increment selling day by 1
        return maxProfit
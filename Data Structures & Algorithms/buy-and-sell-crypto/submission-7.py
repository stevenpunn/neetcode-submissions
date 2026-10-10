class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # use a sliding window
        left = 0
        right = 1
        maxProfit = 0

        # iterate while right can expand
        while right < len(prices):
            # if price on the left < right, subtract to find profit
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                # update the maxProfit
                maxProfit = max(maxProfit, profit)
            else:
                # if price on the right > price on the left, move left pointer (found a cheaper day)
                left = right
            # move right pointer to the next day
            right += 1
        return maxProfit
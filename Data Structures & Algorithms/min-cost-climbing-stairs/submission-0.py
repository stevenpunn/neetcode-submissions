class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cost[i] is the cost of taking step from ith floor
        # can take 1 or 2 steps
        # can choose at index 0 or 1 floor
        # return minmum cost to each the top of the staircase

        # use bottom up dynamic programming
        # from step i, you can come from step i-1 or i-2

        n = len(cost)       # n = number of steps
        dp = [0] * (n + 1)  # dp array of size n + 1
        # dp[0] = 0, dp[1] = 0 because you can start from 0 or 1 for free

        # iterate for each step i from 2 to n
        for i in range(2, n+1):
            # min cost of going down i-1 + cost of going down i-1
            # or going down i-1 + cost of going down i-2
            dp[i] = min(dp[i-1] + cost[i-1],
                        dp[i-2] + cost[i-2])
        
        # reutn dp[n] as the minimum cost to reach the top
        return dp[n]
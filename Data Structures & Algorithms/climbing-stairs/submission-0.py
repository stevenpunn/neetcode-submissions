class Solution:
    def climbStairs(self, n: int) -> int:
        # using dynamic programming bottom-up 
        # to reach step i: i-1 (1 step) or i-2 (2 steps)

        # if n <= 2, 
        if n <= 2:
            return n
        # dp[i] = number of ways to reach step i
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2
        # we only need to calculate steps after step 3
        for i in range(3, n + 1):
            # dp[i-1] and dp[i-2] stores the values previously calculated
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        def dfs(i,buy,cap):

            if(i == n):
                return 0

            if(cap == 0):
                return 0

            if(dp[i][buy][cap] != -1):
                return dp[i][buy][cap]

            if(buy):

                profit = max( -prices[i] + dfs(i+1,0,cap), dfs(i+1,1,cap))

            else :

                profit = max( prices[i] + dfs(i+1,1,cap-1), dfs(i+1,0,cap))

            dp[i][buy][cap] = profit 

            return profit 

        n = len(prices)

        dp = [[[-1]*(k+1) for _ in range(2)] for _ in range(n)]

        return dfs(0,1,k)                        

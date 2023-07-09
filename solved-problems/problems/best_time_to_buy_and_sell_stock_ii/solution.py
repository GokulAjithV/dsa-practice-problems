class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        def dfs(i,buy):

            if(i == n):
                return 0

            if(dp[i][buy] != -1):
                return dp[i][buy]

            if(buy):

                profit = max(-prices[i] + dfs(i+1,0),dfs(i+1,1))

            else :

                profit = max(prices[i] + dfs(i+1,1),dfs(i+1,0))

            dp[i][buy] = profit 

            return dp[i][buy]
        
        n = len(prices)
        dp = [[-1]*(2) for _ in range(n)]

        return dfs(0,1)                   
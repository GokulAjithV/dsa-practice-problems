class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)

        def helper(i,buy):

            if(i >= n):
                return 0

            if(dp[i][buy] != -1):
                return dp[i][buy]    

            if(buy):

                profit = max(-prices[i] + helper(i+1,0),helper(i+1,1))

            else:

                profit = max(prices[i] + helper(i+2,1),helper(i+1,0))

            dp[i][buy] = profit              
   
            return profit 

        dp = [[-1]*2 for _ in range(n)]    

        return helper(0,1)                            

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)

        def helper(i,buy,trans):

            if(trans == 0 or i == n):
                return 0

            if(dp[i][buy][trans] != -1):
                return dp[i][buy][trans]    

            if(buy):

                profit = max(-prices[i] + helper(i+1,0,trans), helper(i+1,1,trans))

            else :

                profit = max(prices[i] + helper(i+1,1,trans-1), helper(i+1,0,trans))

            dp[i][buy][trans] = profit     

            return profit  

        dp = [[[-1]*3 for i in range(2)] for i in range(n)]                             

        return helper(0,1,2)    
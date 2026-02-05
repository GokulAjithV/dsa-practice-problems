class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def helper(i,j):

            if(i == 0 and j == 0):
                return 1

            if(i < 0 or j < 0 ):
                return 0

            if(dp[i][j] != -1):
                return dp[i][j]    
            
            up = helper(i-1,j)
            left = helper(i,j-1)

            dp[i][j] = up + left

            return up + left

        dp = [[-1]*n for _ in range(m)]     

        return helper(m-1,n-1)            




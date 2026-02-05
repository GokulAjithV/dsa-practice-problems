class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        if(obstacleGrid[0][0] == 1):
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[-1]*n for _ in range(m)]

        def helper(i,j):

            if(i == 0 and j == 0):
                return 1

            if(i < 0 or j < 0 or obstacleGrid[i][j] == 1):
                return 0

            if(dp[i][j] != -1):
                return dp[i][j]    

            up = helper(i-1,j)
            left = helper(i,j-1)
            
            dp[i][j] = up + left

            return up + left 

        return helper(m-1,n-1)            

                  
                
                    
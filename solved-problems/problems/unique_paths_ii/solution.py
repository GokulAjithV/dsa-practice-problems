class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        def dfs(i,j):

            if(obstacleGrid[i][j] == 1):
                return 0

            if(i == 0 and j == 0):
                return 1

            if(i < 0 or j < 0):
                return 0


            if(dp[i][j] != -1):
                return dp[i][j]

            up = dfs(i-1,j)
            left = dfs(i,j-1)

            dp[i][j] = up+left 

            return dp[i][j]

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[-1]*n for _ in range(m)]

        return dfs(m-1,n-1)                
                
                    
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        def dfs(i,j):

            if(i == 0 and j == 0):
                return grid[0][0]

            if(i < 0 or j < 0):
                return 300

            if(dp[i][j] != -1):
                return dp[i][j]

            up = grid[i][j] + dfs(i-1,j)
            left = grid[i][j] + dfs(i,j-1)

            dp[i][j] = min(up,left)

            return dp[i][j]

        m = len(grid)
        n = len(grid[0])  
        dp = [[-1]*n for _ in range(m)]
        return dfs(m-1,n-1)    

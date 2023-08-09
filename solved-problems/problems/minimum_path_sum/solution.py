class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:  

        m = len(grid)
        n = len(grid[0])

        def helper(i,j):
            
            if(i == 0 and j == 0):
                return grid[i][j]

            if(i < 0 or j < 0):
                return 1e9

            if(dp[i][j] != -1):
                return dp[i][j]   

            up = grid[i][j] + helper(i-1,j)
            left = grid[i][j] + helper(i,j-1)
            
            dp[i][j] = min(up,left)

            return min(up,left)

        dp = [[-1]*n for _ in range(m)]    

        return helper(m-1,n-1)



        
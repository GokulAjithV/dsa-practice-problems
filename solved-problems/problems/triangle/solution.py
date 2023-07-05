class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        def dfs(i,j):

            if(i == n-1):
                return triangle[n-1][j]

            if(dp[i][j] != -1):
                return dp[i][j]    

            down = triangle[i][j] + dfs(i+1,j)

            diag = triangle[i][j] + dfs(i+1,j+1)

            dp[i][j] = min(down,diag)

            return dp[i][j]

        n = len(triangle)

        i = len(triangle)

        j = len(triangle[n-1])

        dp = [[-1]*j for _ in range(i)]

        return dfs(0,0)

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        n = len(triangle)
        m = len(triangle[n-1])

        dp = [[-1]*m for _ in range(n)]
        
        def helper(row,col):

            if(row == n-1):
                return triangle[row][col]

            if(dp[row][col] != -1):
                return dp[row][col]    

            down = triangle[row][col] + helper(row+1,col)

            rdiag = triangle[row][col] + helper(row+1,col+1)

            dp[row][col] = min(down,rdiag)

            return min(down,rdiag)

        return helper(0,0)      



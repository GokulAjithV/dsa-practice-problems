class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        s2 = s[::-1]

        def helper(m,n):
             
            dp = [[-1]*(n+1) for i in range(m+1)]

            for i in range(m+1):
                dp[i][0] = 0

            for j in range(n+1):
                dp[0][j] = 0

            for i in range(1,m+1):
                for j in range(1,n+1):

                    if(s[i-1] == s2[j-1]):
                        dp[i][j] = 1 + dp[i-1][j-1]
                    
                    else:
                        dp[i][j] = max(dp[i-1][j],dp[i][j-1])

            return dp[m][n] 

        return helper(len(s),len(s2))     



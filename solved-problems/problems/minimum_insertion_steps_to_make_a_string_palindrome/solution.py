class Solution:
    def minInsertions(self, s: str) -> int:

        s2 = s[::-1]
        n = len(s)

        def helper(i,j):

            if(i < 0 or j < 0):
                return 0

            if(dp[i][j] != -1):
                return dp[i][j]

            if(s[i] == s2[j]):
                return 1 + helper(i-1,j-1)

            left = helper(i,j-1)
            right = helper(i-1,j)

            dp[i][j] = max(left,right)

            return dp[i][j]

        dp = [[-1]*(n+1) for _ in range(n+1)]    

        lps = helper(n-1,n-1)

        return n - lps  

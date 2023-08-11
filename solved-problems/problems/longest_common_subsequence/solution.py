class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        m = len(text1)
        n = len(text2)

        def helper(m,n):
            if(m < 0 or n < 0):
                return 0

            if(dp[m][n] != -1):
                return dp[m][n]    

            if(text1[m] == text2[n]):
                return 1 + helper(m-1,n-1)

            left = helper(m-1,n)
            right = helper(m,n-1)

            dp[m][n] = max(left,right)

            return max(left,right)

        dp = [[-1]*(n+1) for _ in range(m)]    

        return helper(m-1,n-1)    


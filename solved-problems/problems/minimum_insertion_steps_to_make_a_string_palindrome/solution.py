class Solution:
    def minInsertions(self, s: str) -> int:

        s2 = s[::-1]

        def helper(i,j):

            if(i < 0 or j < 0):
                return 0

            if(dp[i][j] != -1):
                return dp[i][j]

            if(s[i] == s2[j]):
                dp[i][j] = 1 + helper(i-1,j-1)

            else :
                dp[i][j] = max(helper(i-1,j),helper(i,j-1))


            return dp[i][j]

        dp = [[-1]*(len(s)) for _ in range(len(s))]    

        return len(s) - helper(len(s)-1,len(s)-1)                           
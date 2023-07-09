class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        def helper(i,j):

            if(i < 0):
                return j+1

            if(j < 0):
                return i+1

            if(dp[i][j] != -1):
                return dp[i][j]

            if(word1[i] == word2[j]):
                dp[i][j] = helper(i-1,j-1)
                return dp[i][j]

            else :
                dp[i][j] = 1 + min(helper(i-1,j),helper(i,j-1),helper(i-1,j-1))
                return dp[i][j]
        
        m = len(word1)
        n = len(word2)

        dp = [[-1]*(n) for _ in range(m)]

        return helper(m-1,n-1)                               

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        m = len(word1)
        n = len(word2)

        def helper(i,j):
            if(i < 0 or j < 0):
                return 0

            if(dp[i][j] != -1):
                return dp[i][j]    

            if(word1[i] == word2[j]):
                return 1 + helper(i-1,j-1)

            left = helper(i-1,j)
            right = helper(i,j-1)

            dp[i][j] = max(left,right)

            return max(left,right)    

        dp = [[-1]*(n+1) for _ in range(m+1)]

        lcs = helper(m-1,n-1)

        return (m-lcs) + (n-lcs)    
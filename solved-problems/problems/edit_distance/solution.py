class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        m = len(word1)
        n = len(word2)

        def helper(i,j):

            if(i < 0):
                return j + 1

            if(j < 0):
                return i + 1

            if(dp[i][j] != -1):
                return dp[i][j]    

            if(word1[i] == word2[j]):
                count = helper(i-1,j-1)

            else:
                add = 1 + helper(i,j-1)
                delete = 1 + helper(i-1,j)
                replace = 1 + helper(i-1,j-1)

                count = min(add,delete,replace)

            dp[i][j] = count     

            return dp[i][j]
        
        dp = [[-1]*(n+1) for _ in range(m+1)]

        return helper(m-1,n-1)



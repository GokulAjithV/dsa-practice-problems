class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        m = len(p)
        n = len(s)

        def helper(i,j):

            if(i < 0 and j < 0):
                return True 
            if(i < 0):
                return False
            if(j < 0):
                for k in range(i+1):
                    if(p[k] != '*'):
                        return False
                return True    

            if(dp[i][j] != -1):
                return dp[i][j]                 

            if(p[i] == s[j] or p[i] == '?'):
                res = helper(i-1,j-1) 

            elif(p[i] == '*'):
                res = helper(i-1,j) or helper(i,j-1)

            else:
                res = False
            
            dp[i][j] = res
            
            return res       

        dp = [[-1]*(n+1) for _ in range(m+1)]    

        return helper(m-1,n-1)    
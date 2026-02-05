class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        n = len(s)

        def helper(i,dp):
            if(i == n):
                return True     

            if(dp[i] != -1):
                return dp[i]    

            t = False    

            for j in range(i,n):

                if(s[i:j+1] in wordDict):
                    t = t or helper(j+1,dp)  
                    if(t):
                        break
            dp[i] = t
            return dp[i]    

        dp = [-1]*(n)            

        return helper(0,dp)


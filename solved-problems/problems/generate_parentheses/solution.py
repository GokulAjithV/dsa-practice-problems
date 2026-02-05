class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        limit = n*2

        def dfs(open, close, s):

            if(len(s) == limit):
                res.append(s[:])
                return 

            if(open < n):
                dfs(open+1, close, s+'(')

            if(close < open):
                dfs(open, close+1, s+')')    
            
        dfs(0,0,'')
        return res
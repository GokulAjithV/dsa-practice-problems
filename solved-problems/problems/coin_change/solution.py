class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        def dfs(i,target):
            
            if(i == 0):
                if(target % coins[0] == 0):
                    return target // coins[0]
                else :
                    return 1e9    


            if(dp[i][target] != -1 ):
                return dp[i][target]

            notTake = dfs(i-1,target)

            take = 1e9

            if(target >= coins[i]):

                take = 1 + dfs(i,target - coins[i])

            dp[i][target] = min(take, notTake)

            return dp[i][target]
        
        
        n = len(coins)
        dp = [[-1]*(amount+1) for _ in range(n)]

        ans =  dfs(n-1,amount) 

        if( ans >= 1e9):
            return -1
        else :
            return ans                  
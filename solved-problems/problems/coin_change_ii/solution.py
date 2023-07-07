class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        def dfs(i,target):

            if(i == 0):
                if(target % coins[0] == 0):
                    return 1
                else :
                    return 0

            if(dp[i][target] != -1):
                return dp[i][target] 

            notTake = dfs(i-1,target)

            take = 0

            if(target >= coins[i]):
                take = dfs(i,target - coins[i])

            dp[i][target] = take + notTake 

            return dp[i][target]

        n = len(coins)

        dp = [[-1]*(amount+1) for _ in range(n)]

        return dfs(n-1,amount)                       
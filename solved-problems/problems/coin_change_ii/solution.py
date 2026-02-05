class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        n = len(coins)

        def helper(i,target):
            if(target == 0):
                return 1

            if(i == 0):
                if(target % coins[i] == 0):
                    return 1
                return 0    

            if(dp[i][target] != -1):
                return dp[i][target]        
                
            notTake = helper(i-1,target)
            take = 0
            if(target >= coins[i]):
                take = helper(i,target - coins[i])

            dp[i][target] = take + notTake     
            
            return take + notTake 

        dp = [[-1]*(amount + 1) for _ in range(n)]


        return helper(n-1,amount)  
                               
class Solution:
    def climbStairs(self, n: int) -> int:

        def dp(n):

            prev2 = 1
            prev = 1

            for i in range(2,n+1):
                cur = prev + prev2 
                prev2 = prev 
                prev = cur

            return prev 

        return dp(n)  

        
class Solution:

    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        if(n == 1):
            return nums[0]

        def helper(i,j,dp):

            if(i == j):
                return nums[i]

            if(i < j):
                return 0

            if(dp[i] != -1):
                return dp[i]    

            pick = nums[i] + helper(i-2,j,dp)

            notPick = 0 + helper(i-1,j,dp)
            
            dp[i] = max(pick,notPick) 

            return max(pick,notPick)

        dp1 = [-1]*n
        dp2 = [-1]*n    

        return max(helper(n-2,0,dp1),helper(n-1,1,dp2))            





        
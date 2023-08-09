class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        n = len(nums)

        s = sum(nums)
        if(s % 2 != 0):
            return False

        def helper(i,target):

            if(target == 0):
                return True 

            if(i == 0):
                return target == nums[i]    

            if(dp[i][target] != -1):
                return dp[i][target]    

            notTake = helper(i-1,target)
            
            take = False 

            if(target >= nums[i]):
                take = helper(i-1,target - nums[i])

            dp[i][target] = take or notTake 

            return take or notTake 

        dp = [[-1]*((s//2)+1) for _ in range(n) ]    

        if(helper(n-1,s//2)):
            return True 

        return False       



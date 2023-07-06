class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        def partition(i,target):

            if(target == 0):
                return True 

            if(i == 0):
                return target == nums[0]    

            if(dp[i][target] != -1):
                return dp[i][target]    

            notTake = partition(i-1,target)

            take = False 

            if(target >= nums[i]):

                take = partition(i-1,target - nums[i])

            dp[i][target] = take or notTake 

            return dp[i][target]          

        s = sum(nums)

        if((s % 2) != 0):
            return False 
        
        else : 

            target = s//2 

            dp = [[-1 for i in range(target+1)] for _ in range(len(nums))]

            return partition(len(nums)-1,target)

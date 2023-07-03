class Solution:

    def rob(self, nums: List[int]) -> int:

        
        
        def dfs(n,arr,dp):

            dp[0] = arr[0]
            prev = 0

            for i in range(1,len(arr)):

                take = arr[i]

                if(i > 1):
                    take += dp[i-2]

                notTake = dp[i-1]

                dp[i] = max(take,notTake)

            return dp[n]
        


        if(len(nums) == 1):
            return nums[0]

        
        wf = nums[1:]
        wl = nums[:len(nums)-1]
        return max(dfs(len(wf)-1,wf,{}),dfs(len(wl)-1,wl,{}))





        
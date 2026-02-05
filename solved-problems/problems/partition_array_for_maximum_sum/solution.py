class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:

        n = len(arr)

        dp = [-1]*(n)


        def dfs(i):

            if(i == n):
                return 0

            if(dp[i] != -1):
                return dp[i]    

            length = 0
            maxVal = 0   
            maxSum = 0

            for j in range(i,min(n,i+k)):

                length += 1 
                maxVal = max(maxVal,arr[j])

                Sum = (length*maxVal) + dfs(j+1)
                maxSum = max(maxSum,Sum)

            dp[i] = maxSum    

            return maxSum 

        return dfs(0)  


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        def dfs(i, count):
            if i < 0:
                if target == count:
                    return 1
                else:
                    return 0

            if dp[i][count] != -1:
                return dp[i][count]
            
            pos = dfs(i - 1, count + nums[i])
            neg = dfs(i - 1, count - nums[i])
            dp[i][count] = pos + neg

            return dp[i][count]

        total = sum(nums)
        n = len(nums)
        dp = [[-1] * (total * 2 + 1) for _ in range(n)]

        return dfs(n - 1, 0)
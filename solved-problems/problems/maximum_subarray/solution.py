class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        result = 0

        maxi = float('-inf')

        for i in range(len(nums)):

            result += nums[i]
            maxi = max(maxi,result)

            if( result < 0):
                result = 0

        return maxi       

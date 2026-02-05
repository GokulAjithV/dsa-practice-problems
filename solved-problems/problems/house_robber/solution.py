class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dic = {}
        def dfs(i):

            dic[0] = nums[0]

            prev = 0

            for i in range(1,len(nums)):

                pick = nums[i]
                if(i > 1):
                    pick += dic[i-2]

                notPick = dic[i-1]

                dic[i] = max(pick,notPick)

            return dic[i]          

        return dfs(len(nums)-1)      

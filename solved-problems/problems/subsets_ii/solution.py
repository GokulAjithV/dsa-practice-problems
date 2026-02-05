class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        def dfs(k,sub,res):
            res.append(sub.copy())
            for i in range(k,len(nums)):
                if(i != k and nums[i] == nums[i-1]):
                    continue
                sub.append(nums[i])
                dfs(i+1,sub,res)
                sub.pop()
        res = []
        nums.sort()
        dfs(0,[],res)
        return res            

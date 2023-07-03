class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(i,target,sub):
            
            if(i == len(candidates)):
                if(target == 0):
                    res.append(sub[:])
                return 

            if(candidates[i] <= target):

                sub.append(candidates[i])
                target -= candidates[i]

                dfs(i,target,sub)

                sub.pop()
                target += candidates[i] 

            dfs(i+1,target,sub)
        
        res = []
        dfs(0,target,[]) 
        return res          

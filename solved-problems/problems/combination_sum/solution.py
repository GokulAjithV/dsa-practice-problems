class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []

        n = len(candidates)

        def helper(i,temp,target):

            if(target == 0):
                res.append(temp[:])
                return

            if(target < 0 or i == n):
                return     

            temp.append(candidates[i])
            helper(i,temp,target - candidates[i])

            temp.pop()
            helper(i+1,temp,target)    

        helper(0,[],target)

        return res


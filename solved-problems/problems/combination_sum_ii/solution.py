class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        n = len(candidates)

        def helper(ind,temp,target):

            if(target == 0):
                res.append(temp[:])
                return 

            for i in range(ind,n):

                if(i > ind and candidates[i] == candidates[i-1]):
                    continue

                if(candidates[i] > target):
                    break

                temp.append(candidates[i])
                helper(i+1,temp,target - candidates[i])
                temp.pop()
                
        candidates.sort()
        helper(0,[],target)
        return res


            
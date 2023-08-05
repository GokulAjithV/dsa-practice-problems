class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []

        n = len(candidates)

        def helper(i,arr,summ):

            if(target == summ):
                res.append(arr[:])
                return 

            if(summ > target or i >= n):
                return 

            arr.append(candidates[i])
            summ += candidates[i]
            helper(i,arr,summ)

            arr.pop()
            summ -= candidates[i]
            helper(i+1,arr,summ)

        helper(0,[],0)

        return res


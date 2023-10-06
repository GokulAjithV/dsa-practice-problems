class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        def comb(i,temp,amount):

            if(i == len(candidates)):
                if(amount == 0):
                    res.append(temp[:])
                return     

            comb(i+1,temp,amount)

            if(amount >= candidates[i]):
                temp.append(candidates[i])
                comb(i,temp,amount - candidates[i])
                temp.pop()
        
        comb(0,[],target)
        return res




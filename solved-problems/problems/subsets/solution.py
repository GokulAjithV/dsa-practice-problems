class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        res = []

        def helper(ind,temp):

            if(ind == n):
                res.append(temp[:])
                return 

            temp.append(nums[ind])
            helper(ind+1,temp)
            temp.pop()
            helper(ind+1,temp)

        helper(0,[])   
        return res       
                

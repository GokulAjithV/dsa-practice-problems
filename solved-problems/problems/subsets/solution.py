class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        ans = []
        def helper(i,arr):

            if(i == n):
                ans.append(arr[:])
                return 

            arr.append(nums[i])
            helper(i+1,arr)
            arr.remove(nums[i])
            helper(i+1,arr)
        helper(0,[])
        return ans        
                

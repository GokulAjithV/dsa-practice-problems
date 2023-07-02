class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def permutations(ind,nums):
            if(ind == len(nums)):
                res.append(nums[:])
                return

            for i in range(ind,len(nums)):
                nums[ind],nums[i] = nums[i],nums[ind]
                permutations(ind+1,nums)
                nums[ind],nums[i] = nums[i],nums[ind]

        res = []
        permutations(0,nums)
        return res            
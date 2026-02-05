class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        l = 0
        i = 0

        length = len(nums)

        while i < len(nums):

            if(val == nums[i]):
                nums.pop(i)
                l += 1

            else:
                i += 1

        k = length - l            
            


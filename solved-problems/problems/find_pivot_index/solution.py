class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftsum = 0
        for i,n in enumerate(nums):
            total -= n 
            if leftsum == total:
                return i 
            leftsum += n 
        return -1    
        
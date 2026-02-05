class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def first(ans):

            low = 0
            high = len(nums) - 1

            while low <= high:

                mid = (low + high)//2

                if(nums[mid] >= target):
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1

            return ans 

        def last(ans):

            low = 0
            high = len(nums) - 1

            while low <= high:

                mid = (low+high)//2 

                if(nums[mid] <= target):
                    ans = mid 
                    low = mid + 1
                else:
                    high = mid - 1

            return ans 



        f = first(0)
        if(not nums or nums[f] != target):
            return [-1,-1]
        l = last(0)
        return [f,l]                                   




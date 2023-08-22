class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s1 = (n*(n+1))/2
        s2 = sum(nums)
        s = s1 - s2    

        return int(s)



        


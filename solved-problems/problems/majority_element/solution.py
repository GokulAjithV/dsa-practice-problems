class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count = 0
        element = 0

        for n in nums:

            if(count == 0):
                element = n

            if(element == n):
                count += 1
            else:
                count -= 1

        return element                
        
        
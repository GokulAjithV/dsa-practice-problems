class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashMap = {}

        for i, val in enumerate(nums):

            diff = target - val

            if(val in hashMap):
                return [hashMap[val],i]

            else:
                hashMap[diff] = i


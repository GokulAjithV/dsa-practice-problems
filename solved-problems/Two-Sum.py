1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        n = len(nums)
4        for i in range(n - 1):
5            for j in range(i+1, n):
6                if (target == nums[i] + nums[j]):
7                    return [i,j]
8
9        
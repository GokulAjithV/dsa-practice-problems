class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if(len(nums) == 0):
            return 0

        st = set(nums)

        res = 1

        for i in st:

            if(i-1 not in st):

                count = 1
                a = i

                while a + 1 in st:
                    count += 1
                    a += 1

                res = max(res,count)

        return res            





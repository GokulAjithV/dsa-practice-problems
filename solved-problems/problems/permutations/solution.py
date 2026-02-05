class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        res = []

        def helper(i,visited,temp):

            if(len(visited) == n):
                res.append(temp[:])
                return 

            for i in range(n):

                if(i not in visited):
                    visited[i] = 1
                    temp.append(nums[i])
                    helper(i,visited,temp)
                    visited.popitem()
                    temp.pop()

        helper(0,{},[])
        return res           
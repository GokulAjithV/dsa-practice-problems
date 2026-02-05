class Solution:
    def maxJump(self, stones: List[int]) -> int:

        n = len(stones)

        if(n == 2):
            return stones[-1]

        diff = 0

        for i in range(n-2):

            diff = max(diff,stones[i+2]-stones[i])

        return diff        
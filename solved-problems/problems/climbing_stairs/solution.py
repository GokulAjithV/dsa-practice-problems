class Solution:
    cache = {}
    def climbStairs(self, n: int) -> int:

        if n == 0 or n == 1:
            return 1 

        if n in self.cache :
            return self.cache[n]

        res = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        self.cache[n] = res 

        return res             

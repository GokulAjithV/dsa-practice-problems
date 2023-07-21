class Solution:
    def isHappy(self, n: int) -> bool:

        Set = set()

        while n != 1:

            if(n in Set):
                return False 

            Set.add(n)
            
            var = 0
            while n > 0:
                last = n % 10
                var += last**2
                n //= 10

            n = var 

        return True        


                



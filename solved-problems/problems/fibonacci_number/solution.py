class Solution:
    def fib(self, n: int) -> int:

        def find_fibonacci(i):

            if (i == 0) or (i == 1):
                return i
            
            return find_fibonacci(i - 1) + find_fibonacci(i - 2)
        
        return find_fibonacci(n)
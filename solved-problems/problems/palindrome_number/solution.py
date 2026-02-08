class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False
        if x < 10:
            return True
        
        input_int = x
        reversed_int = 0

        while input_int > 0:
            last_digit = input_int % 10
            input_int = input_int // 10
            reversed_int = (reversed_int * 10) + last_digit

        return reversed_int == x
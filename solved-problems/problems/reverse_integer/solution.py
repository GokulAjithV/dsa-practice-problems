class Solution:
    def reverse(self, x: int) -> int:    

        if (x in [0, 1, -1]):
            return x

        reserved_input = 0

        is_negative = x < 0

        input_integer = -x if is_negative else x

        while input_integer > 0:
            last_digit = input_integer % 10    
            input_integer = input_integer // 10
            reserved_input = (reserved_input * 10) + last_digit

        reserved_input = -reserved_input if is_negative else reserved_input

        if (-2**31 > reserved_input or reserved_input >= 2**31):
            return 0

        return reserved_input


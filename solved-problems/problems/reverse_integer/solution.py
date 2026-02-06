class Solution:
    def reverse(self, x: int) -> int:    

        if (x in [0, 1, -1]):
            return x
        
        is_negative = x < 0

        stringified_input = ""

        input_integer = -x if is_negative else x

        while True:
            last_digit = input_integer % 10
            if (last_digit == 0):
                input_integer = input_integer // 10
            else: 
                break

        while input_integer > 0:
            last_digit = input_integer % 10
            stringified_input += str(last_digit)    
            input_integer = input_integer // 10

        result = -int(stringified_input) if is_negative else int(stringified_input)

        if (-2**31 > result or result >= 2**31):
            return 0

        return result


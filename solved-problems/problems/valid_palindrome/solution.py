class Solution:
    def isPalindrome(self, s: str) -> bool:

        alphanum_s = "".join(filter(str.isalnum, s)).lower()
        print(alphanum_s)
        
        def check_palindrome(i, j):
            if (i >= j):
                return True
            
            if (alphanum_s[i] != alphanum_s[j]):
                return False

            return check_palindrome(i+1, j-1)

        return check_palindrome(0, len(alphanum_s) - 1)
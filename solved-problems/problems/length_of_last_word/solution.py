class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        j = 0   
        string = s[::-1]
        count = 0

        while (string[j] == " "):
            
            j += 1


        while (j < len(string) and string[j] != " "):

            count += 1
            j += 1

        return count        




class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if(haystack == needle):
            return 0
        j = len(needle)
        for i in range(len(haystack)+1):
            if(haystack[i:j] == needle):
                return i

            j += 1    

        return -1            


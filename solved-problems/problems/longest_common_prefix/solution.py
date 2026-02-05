class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if(len(strs) == 0):
            return ""
        if(len(strs) == 1):
            return strs[0]

        pre = strs[0]
        plen = len(pre)

        for i in strs[1:]:

            while pre != i[:plen] :

                plen -= 1

                pre = pre[:plen]

                if(plen == 0):
                    return ""

        return pre                


        
                

            
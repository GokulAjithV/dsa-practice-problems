class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        mapST = {}
        mapTS = {}

        for s1,s2 in zip(s,t):

            if((s1 in mapST and mapST[s1] != s2) or (s2 in mapTS and mapTS[s2] != s1) ):
                return False

            mapST[s1] = s2
            mapTS[s2] = s1

        return True         


          


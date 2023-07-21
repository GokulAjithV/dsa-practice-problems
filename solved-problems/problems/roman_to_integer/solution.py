class Solution:
    def romanToInt(self, s: str) -> int:

        hashMap = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

        ans = 0

        for i in range(len(s)-1):

            if(hashMap[s[i]] < hashMap[s[i+1]]):
                ans -= hashMap[s[i]]

            else:
                ans += hashMap[s[i]]    

        ans += hashMap[s[-1]]

        return ans        





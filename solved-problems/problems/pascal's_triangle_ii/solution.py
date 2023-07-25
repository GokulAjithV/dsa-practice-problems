class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        ans = []

        for i in range(rowIndex+1):
            res = 1
            for j in range(i):
                res = res * (rowIndex-j)
                res = res / (j+1)
            ans.append(int(res))

        return ans        


        
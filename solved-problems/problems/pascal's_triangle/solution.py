class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1]]

        for i in range(1,numRows):
            temp = []
            last = res[-1]
            for j in range(1,len(last)):
                temp.append(last[j-1] + last[j])

            temp[:] = [1] + temp + [1]

            res.append(temp)

        return res        
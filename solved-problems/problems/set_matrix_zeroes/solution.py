class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        dr = [-1 for i in range(len(matrix))]
        dc = [-1 for j in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0 :
                    dr[i],dc[j] = 0,0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != 0 :
                    if dr[i] == 0 or dc[j] == 0 :
                        matrix[i][j] = 0
        return matrix        

                      
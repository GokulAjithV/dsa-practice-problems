class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        visited = [[0]*n for _ in range(m)]

        queue = []
        
        freshCnt = 0
        for i in range(m):
            for j in range(n):
                if(grid[i][j] == 2):
                    queue.append([[i,j],0])
                    visited[i][j] = 2
                elif(grid[i][j] == 1):
                    freshCnt += 1
        
        count = 0
        cnt = 0
        drow = [-1,0,1,0]
        dcol = [0,1,0,-1]
        while queue :

            node = queue.pop(0)
            row,col = node[0]
            time = node[1]
            count = max(count,time)

            for i in range(4):
                nrow = row + drow[i]
                ncol = col + dcol[i]

                if(
                    0 <= nrow < m and 
                    0 <= ncol < n and 
                    grid[nrow][ncol] == 1 and 
                    not visited[nrow][ncol]
                ):
                    visited[nrow][ncol] = 2
                    queue.append([[nrow,ncol],time + 1])
                    cnt += 1


        if(freshCnt != cnt):
            return -1

        return count                



 


                          

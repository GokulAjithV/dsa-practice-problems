class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [0]*n

        adj = [[] for i in range(n)]

        for i in range(n):
            for j in range(n):
                if(i != j and isConnected[i][j]):
                    adj[i].append(j)




        def bfs(i):
            queue = [i]

            while queue:
                node = queue.pop(0)
                visited[node] = 1

                for neighbor in adj[node]:
                    if(not visited[neighbor] and isConnected[neighbor]):
                        queue.append(neighbor)



        ans = 0   
        for i in range(n):
            if(not visited[i]):
                bfs(i)
                ans += 1

        return ans                            

[[1,0,0,1],
[0,1,1,0],
[0,1,1,1],
[1,0,1,1]]

        
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        m = len(isConnected)
        visited = [0]*m
        graph = [[] for _ in range(m)]

        for i in range(m):
            for j in range(m):
                if(i != j and isConnected[i][j]):
                    graph[i].append(j)

        def dfs(node):

            visited[node] = 1

            for neighbor in graph[node]:
                if(not visited[neighbor]):
                    dfs(neighbor)
        
        ans = 0
        for node in range(m):
            if(not visited[node]):
                ans += 1
                dfs(node)

        return ans        
            




        
                                 



        
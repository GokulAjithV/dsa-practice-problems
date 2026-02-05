class Solution:

    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        n = len(graph)
        colored = [-1]*n
        
        def dfs(node):

            for child in graph[node]:
                if(colored[child] == -1):
                    colored[child] = not colored[node]
                    if(not dfs(child)):
                        return False
                elif(colored[child] == colored[node]):
                    return False     

            return True         
            

        for i in range(n):
            if(colored[i] == -1):
                colored[i] = 0
                if(not dfs(i)):
                    return False

        return True                 



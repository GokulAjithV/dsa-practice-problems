class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        graph = {}

        for u,v in edges:
            if(u in graph):
                graph[u].append(v)
            else :
                graph[u] = [v]

            if(v in graph):
                graph[v].append(u)
            else :
                graph[v] = [u]          
        visited = set()
        def dfs(source,destination):

            if(source == destination):
                return True

            visited.add(source)
            for neighbour in graph[source]:
                if(neighbour not in visited):
                    if(dfs(neighbour,destination) == True):
                        return True

            return False

        return dfs(source,destination)            

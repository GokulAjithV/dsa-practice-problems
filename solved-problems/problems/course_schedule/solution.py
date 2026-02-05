class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        n = numCourses 
        graph = [[] for _ in range(n)]        
        
        for edge in prerequisites:
            graph[edge[0]].append(edge[1])

        inedge = [0]*n

        for i in range(n):
            for node in graph[i]:
                inedge[node] += 1

        queue = []

        for i in range(n):
            if(not inedge[i]):
                queue.append(i)
        topo = []

        while queue:
            node = queue.pop(0)
            topo.append(node)

            for neighbour in graph[node]:
                inedge[neighbour] -= 1
                if(not inedge[neighbour]):
                    queue.append(neighbour)

        if(len(topo) != n):
            return False

        return True                 








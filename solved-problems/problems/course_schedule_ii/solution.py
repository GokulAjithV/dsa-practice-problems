class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        n = numCourses
        graph = [[] for _ in range(n)]

        for edge in prerequisites:
            graph[edge[0]].append(edge[1])

        indegree = [0]*n

        for i in range(n):
            for node in graph[i]:
                indegree[node] += 1

        topo = []
        queue = []

        for node in range(n):
            if(not indegree[node]):
                queue.append(node)

        while queue:
            node = queue.pop(0)
            topo.append(node)

            for neighbour in graph[node]:
                indegree[neighbour] -= 1
                if(not indegree[neighbour]):
                    queue.append(neighbour)

        if(len(topo) == n):
            return topo[::-1]

        return []                







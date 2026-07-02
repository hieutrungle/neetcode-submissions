class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = [[] for _ in range(numCourses)]
        indegrees = [0 for _ in range(numCourses)] 

        for u, v in prerequisites:
            adj[v].append(u)
            indegrees[u] += 1

        queue = deque([])
        for node, cnt in enumerate(indegrees):
            if indegrees[node] == 0:
                queue.append(node)

        while queue:
            node = queue.popleft()
            for next_node in adj[node]:
                indegrees[next_node] -= 1
                if indegrees[next_node] == 0:
                    queue.append(next_node)

        return True if sum(indegrees) == 0 else False
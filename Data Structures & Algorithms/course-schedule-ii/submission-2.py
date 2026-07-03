class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses

        for u, v in prerequisites:
            adj[v].append(u)
            indegrees[u] += 1
        res = []
        queue = deque([])
        for node, cnt in enumerate(indegrees):
            if cnt == 0:
                queue.append(node)
                
        while queue:
            node = queue.popleft()
            res.append(node)
            for next_node in adj[node]:
                indegrees[next_node] -= 1
                if indegrees[next_node] == 0:
                    queue.append(next_node)

        return res if len(res) == numCourses else []
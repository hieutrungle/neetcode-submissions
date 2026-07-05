class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.sizes = [1] * n

    def find(self, u):
        if self.parents[u] == u:
            return self.parents[u]

        self.parents[u] = self.find(self.parents[u])
        return self.parents[u]

    def unite(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return False

        if self.sizes[root_u] < self.sizes[root_v]:
            root_u, root_v = root_v, root_u

        self.parents[root_v] = root_u
        self.sizes[root_u] += self.sizes[root_v]
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        nodes = set()
        for u, v in edges:
            nodes.add(u)
            nodes.add(v)

        uf = UnionFind(len(nodes))

        res = []
        for u, v in edges:
            if not uf.unite(u - 1, v - 1):
                res = [u, v]

        return res
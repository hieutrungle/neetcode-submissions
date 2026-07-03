class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.sizes = [1] * n
        self.components = n

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

        if self.sizes[u] < self.sizes[v]:
            root_u, root_v = root_v, root_u

        self.parents[root_v] = root_u
        self.sizes[root_u] += self.sizes[root_v]
        self.components -= 1
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        uf = UnionFind(n)
        for u, v in edges:
            uf.unite(u, v)

        return uf.components
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []

        def dfs(j, i, cur):
            if i >= len(s):
                if i == j:
                    self.res.append(cur.copy())
                return

            if self.is_pali(s, j, i):
                cur.append(s[j: i + 1])
                dfs(i + 1, i + 1, cur)
                cur.pop()

            dfs(j, i + 1, cur)

            return

        dfs(0, 0, [])
        return self.res

    def is_pali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
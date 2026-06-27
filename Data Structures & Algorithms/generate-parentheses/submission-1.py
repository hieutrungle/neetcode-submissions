class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []

        def dfs(n_opens, k, ans):
            if k == 0:
                ans = ans + [')'] * n_opens
                self.res.append("".join(ans))
                return
            
            dfs(n_opens + 1, k - 1, ans + ['('])
            if n_opens > 0:
                dfs(n_opens - 1, k, ans + [')'])

            return

        dfs(0, n, [])
        return self.res
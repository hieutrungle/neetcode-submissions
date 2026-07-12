class Solution:
    def countSubstrings(self, s: str) -> int:
        
        res = 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for l in range(n - 1, -1, -1):
            for r in range(l, n):
                if s[l] == s[r] and (r - l + 1 <= 2 or dp[l + 1][r - 1]):
                    dp[l][r] = True
                    res += 1
        
        return res
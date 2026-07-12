class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        start_idx, length = 0, 0

        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for l in range(n - 1, -1, -1):
            for r in range(l, n):
                if s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1]):
                    dp[l][r] = True
                    if length < (r - l + 1):
                        start_idx = l
                        length = r - l + 1

        return s[start_idx : start_idx + length]
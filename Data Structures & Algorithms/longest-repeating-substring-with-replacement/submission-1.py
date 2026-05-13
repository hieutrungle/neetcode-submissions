class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        cnts = [0] * 26
        res = 0
        for r in range(len(s)):
            c = s[r]
            cnts[ord(s[r]) - ord('A')] += 1

            while l < r and (r - l + 1) - max(cnts) > k:
                cnts[ord(s[l]) - ord('A')] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
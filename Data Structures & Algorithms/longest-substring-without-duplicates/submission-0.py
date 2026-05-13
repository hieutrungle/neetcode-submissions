class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        d = set([])
        res = 0
        for r in range(len(s)):
            while l < r and s[r] in d:
                d.remove(s[l])
                l += 1

            res = max(res, r - l + 1)
            d.add(s[r])

        return res
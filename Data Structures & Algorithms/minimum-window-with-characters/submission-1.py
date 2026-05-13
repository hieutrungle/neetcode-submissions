from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        counter_s = Counter(s)
        counter_t = Counter(t)

        for c, cnt in counter_t.items():
            if c not in counter_s:
                return ""
            if counter_s[c] < cnt:
                return ""

        cnts_s = [0] * (26 * 2)
        cnts_t = [0] * (26 * 2)

        for c in t:
            cnts_t[ord(c) - ord('a')] += 1

        def is_satisfy():
            for i in range((26 * 2)):
                if cnts_s[i] < cnts_t[i]:
                    return False
            return True

        res = [-1, float('inf')]
        l = 0
        for r, c in enumerate(s):
            idx = ord(c) - ord('a')
            cnts_s[idx] += 1

            while l <= r and is_satisfy():
                if r - l < res[1] - res[0]:
                    res = [l, r]
                left_idx = ord(s[l]) - ord('a')
                cnts_s[left_idx] -= 1
                l += 1

        return "" if res[1] == float('inf') else s[res[0]: res[1] + 1]
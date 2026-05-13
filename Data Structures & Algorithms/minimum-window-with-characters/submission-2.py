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

        have, need = 0, len(counter_t)
        res = [-1, float('inf')]
        l = 0
        counter_s = {}
        for r, c in enumerate(s):
            counter_s[c] = counter_s.get(c, 0) + 1

            if c in counter_t and counter_s[c] == counter_t[c]:
                have += 1

            while have == need:
                if r - l + 1 < res[1] - res[0] + 1:
                    res = [l, r]

                counter_s[s[l]] -= 1
                if s[l] in counter_t and counter_s[s[l]] < counter_t[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return "" if res[1] == float('inf') else s[l: r + 1]
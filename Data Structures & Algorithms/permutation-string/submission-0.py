class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        d1 = {}
        for c1 in s1:
            d1[c1] = d1.get(c1, 0) + 1
        
        l = 0
        d2 = {}
        for r, c2 in enumerate(s2):
            if c2 not in d1:
                d2 = {}
                l = r + 1
                continue
            d2[c2] = d2.get(c2, 0) + 1
            if d1 == d2:
                return True

            while l < r and d2[c2] > d1[c2]:
                d2[s2[l]] -= 1
                l += 1

        return False
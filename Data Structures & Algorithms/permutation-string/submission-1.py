class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        cnts1 = [0] * 26
        for c1 in s1:
            cnts1[ord(c1) - ord('a')] += 1
            
        l = 0
        cnts2 = [0] * 26
        for r, c2 in enumerate(s2):
            idx2 = ord(c2) - ord('a')
            if cnts1[idx2] == 0:
                cnts2 = [0] * 26
                l = r + 1
                continue

            cnts2[idx2] += 1
            if cnts1 == cnts2:
                return True

            while l < r and cnts2[idx2] > cnts1[idx2]:
                l_idx = ord(s2[l]) - ord('a')
                cnts2[l_idx] -= 1
                l += 1

        return False
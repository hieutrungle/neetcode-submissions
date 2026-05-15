class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        if len(piles) == h:
            return max(piles)
        
        def is_satisfied(k):
            cnt = 0
            i = len(piles) - 1
            while i >= 0:
                cnt += math.ceil(piles[i] / k)
                i -= 1
                if cnt > h:
                    return False
            return True

        res = -1
        l, r = 1, max(piles) + 1
        while l < r:
            m = (l + r) // 2
            if is_satisfied(m):
                res = m
                r = m
            else:
                l = m + 1
        
        return res
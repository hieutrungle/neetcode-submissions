class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()

        while n not in seen:
            seen.add(n)
            n_str = str(n)
            s = 0
            for c in n_str:
                s += int(c) ** 2
            if s == 1:
                return True
            else:
                n = int(s)
        return False
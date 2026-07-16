class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()

        while n not in seen:
            seen.add(n)
            s = 0
            while n:
                digit = n % 10
                s += digit ** 2
                n = n // 10
            if s == 1:
                return True
            n = s 
        return False
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        res = []
        n = len(digits)
        c = 1
        for i in range(n -1, -1, -1):
            tmp = digits[i] + c
            c = tmp // 10
            res.append(tmp % 10)

        if c:
            res.append(c)
        
        return res[::-1]

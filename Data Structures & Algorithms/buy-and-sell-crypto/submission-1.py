class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        res = 0
        min_buy = float('inf')
        for p in prices:
            res = max(res, p - min_buy)
            min_buy = min(min_buy, p)
        return res
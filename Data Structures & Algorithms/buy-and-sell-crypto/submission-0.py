class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        res = 0
        min_buy = float('inf')
        for p in prices:
            profit = p - min_buy
            res = max(res, profit)
            min_buy = min(min_buy, p)
        return res
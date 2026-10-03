class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pMin, res = prices[0], 0
        for p in prices:
            pMin = min(pMin, p)
            res = max(res, p - pMin)
        return res
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        minBuy = prices[0]
        for sell in prices:
            if sell < minBuy:
                minBuy = sell
            ans = max(sell - minBuy, ans)
        return ans
            
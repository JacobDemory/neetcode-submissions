class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        ans = 0
        while sell < len(prices):
            if prices[sell] < prices[buy]:
                buy = sell
            ans = max(prices[sell] - prices[buy], ans)
            sell += 1
        return ans
            
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        buy = 0
        for sell in range(len(prices)):
            ans = max(prices[sell] - prices[buy], ans)
            while prices[sell] < prices[buy]:
                buy += 1
        return ans
            
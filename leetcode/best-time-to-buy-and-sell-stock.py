class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0    # buy

        while right < len(prices):
        right = 1   # sell
        maxProfit = 0
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else:
                left = right
            right += 1
        return maxProfit

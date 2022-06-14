class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # kadane algorithm
        n = len(prices)
        profit = 0
        max_profit = 0
        for i in range(1,n):
            # 利益は常に変化し続けるから+
            profit += prices[i] - prices[i - 1]
            # 最初見つけるときや値が下がった時
            profit = max(profit, 0)
            # maxは変わった時のみ、常に外側
            max_profit = max(profit, max_profit)
        return max_profit

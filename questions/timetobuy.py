class Solution:
    # def time_buy(self,price,prices):
    #     flag = 0
    #     for i in prices:
    #         if price < i:
    #             flag = 1
    #     if flag = 1:
    #         return True
    #     else:
    #         return False
        
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        for i in range(1,n):
            profit += max(prices[i] - prices[i - 1], 0)
        return profit
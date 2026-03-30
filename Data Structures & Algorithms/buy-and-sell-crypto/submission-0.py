class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        i = 0
        r = 1

        max_profit = 0
        

        while r < len(prices):
            profit = prices[r] - prices[i]
            if prices[r] < prices[i]:
                i = r

            r+=1


            max_profit = max(max_profit,profit)



        return max_profit
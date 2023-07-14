class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minBuy = float('inf')

        maxProfit = 0

        i = 0

        while i < len(prices)-1:

            minBuy = min(minBuy,prices[i])

            profit = prices[i+1] - minBuy

            maxProfit = max(maxProfit,profit)

            i += 1

        return maxProfit     



class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minBuy = float('inf')
        maxProfit = 0

        for i in prices:

            minBuy = min(minBuy,i)

            maxProfit = max(maxProfit,i - minBuy)

        return maxProfit     



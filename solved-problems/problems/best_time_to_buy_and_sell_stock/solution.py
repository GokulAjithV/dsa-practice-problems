class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        mini = float('inf')

        max_profit = 0

        for price in prices:

            mini = min(mini,price)

            max_profit = max(max_profit,price - mini)

        return max_profit    

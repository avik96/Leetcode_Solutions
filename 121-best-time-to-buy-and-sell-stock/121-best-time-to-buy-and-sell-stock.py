class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        minp = prices[0]
        
        for i in range(1, len(prices)):
            minp = min(minp, prices[i])
            profit = prices[i] - minp
            maxp = max(maxp, profit)
                    
        return maxp
        
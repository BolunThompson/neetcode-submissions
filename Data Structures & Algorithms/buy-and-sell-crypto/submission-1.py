class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp_table = []
        # each entry is best from 0..i
        # algorithm: at i = 0, 0
        # algorithm: at some i, max(DP[i - 1], P[i] - found_min)
        # Solution: DP[-1]
        # Goal: in place
        found_min = prices[0]
        prices[0] = 0
        for i in range(1, len(prices)):
            prices[i], found_min = max(prices[i - 1], prices[i] - found_min), min(prices[i], found_min)
        return prices[-1]            

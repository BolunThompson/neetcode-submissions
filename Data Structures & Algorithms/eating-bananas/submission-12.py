import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        highest_k = max(piles)
        lowest_k = 1
        while True:
            middle_k = lowest_k + (highest_k - lowest_k + 1) // 2
            h_used = sum((v + middle_k - 1) // middle_k for v in piles)
            if h_used > h:
                lowest_k = middle_k + 1
            elif highest_k != middle_k:
                highest_k = middle_k
            else:
                break
        lowest_used = sum((v + lowest_k - 1) // lowest_k for v in piles)
        if lowest_used <= h:
            return lowest_k

        return highest_k
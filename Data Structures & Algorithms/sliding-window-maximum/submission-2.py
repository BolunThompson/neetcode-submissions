import heapq
from itertools import islice

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        s = sorted(enumerate(nums), key=lambda v: v[1])
        windowNum = len(nums) - k + 1
        maximums = [-1 for _ in range(windowNum)]
        fills = 0
        for i, v in reversed(s):
            for wi in range(max(i - k + 1, 0), min(i + 1, windowNum)):
                if maximums[wi] == -1:
                    maximums[wi] = v
                    fills += 1
            if fills == windowNum:
                return maximums
            assert fills < windowNum
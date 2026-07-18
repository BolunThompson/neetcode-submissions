class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 1:
            return 0
        s = 0
        e = len(height) - 1
        area = 0
        max_height = min(height[s], height[e])
        while e > s:
            old_s, old_e = height[s], height[e]
            # advance smaller
            if old_s < old_e:
                while height[s] <= old_s and e > s:
                    # we know that this > 0 since height[s] <= old_s == max_height
                    assert max_height - height[s] >= 0
                    area += max_height - height[s]
                    s += 1
            else: # fine to advance if equal
                while height[e] <= old_e and e > s:
                    assert max_height - height[e] >= 0
                    area += max_height - height[e]
                    e -= 1
            max_height = min(height[s], height[e])
        return area
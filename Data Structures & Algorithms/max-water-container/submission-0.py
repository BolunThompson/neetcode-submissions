class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        maxFound = 0
        while i < j:
            height = min(heights[i], heights[j])
            width = j - i
            maxFound = max(maxFound, height * width)
            if heights[i] < heights[j]:
                i += 1
            elif heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
                j -= 1
        return maxFound
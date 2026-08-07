class Solution:
    def findMin(self, nums: List[int]) -> int:
        def search(start, end):
            if end - start == 1:
                return min(nums[start], nums[0]) # if crossover never occured
            middle = start + (end - start) // 2
            mid = nums[middle]
            if mid < nums[middle - 1]:
                return mid
            if nums[start] < nums[middle]:
                return search(middle, end)
            else:
                return search(start, middle)
        
        return search(0, len(nums))
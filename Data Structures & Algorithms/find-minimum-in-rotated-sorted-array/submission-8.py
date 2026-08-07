class Solution:
    def findMin(self, nums: List[int]) -> int:
        def search(start, end):
            if end - start == 1:
                return nums[0] # crossover never occured, so the first is the minimum
            middle = start + (end - start) // 2
            mid = nums[middle]
            if mid < nums[middle - 1]: # crossover
                return mid
            if nums[start] < nums[middle]:
                return search(middle, end)
            return search(start, middle)
        
        return search(0, len(nums))
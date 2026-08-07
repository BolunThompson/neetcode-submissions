class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def searchMIndex(start, end):
            if end - start == 1:
                return 0 # no crossover found
            middle = start + (end - start) // 2
            mid = nums[middle]
            if mid < nums[middle - 1]: # crossover
                return middle
            if nums[start] < nums[middle]:
                return searchMIndex(middle, end)
            return searchMIndex(start, middle)
        
        offset = searchMIndex(0, len(nums))

        def search(start, end):
            assert end <= len(nums)
            if start == end:
                return -1
            middle_ind = start + ((end - start) // 2)
            middle = nums[(middle_ind + offset) % len(nums)]
            if middle < target:
                return search(middle_ind + 1, end)
            elif middle > target:
                return search(start, middle_ind)                 
            
            return middle_ind

        ind = search(0, len(nums))
        return (ind + offset) % len(nums) if ind >= 0 else -1
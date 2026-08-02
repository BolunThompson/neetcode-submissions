

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def search(start, end):
            assert end <= len(nums)
            if start == end:
                return -1
            middle_ind = start + ((end - start) // 2)
            middle = nums[middle_ind]
            if middle < target:
                return search(middle_ind + 1, end)
            elif middle > target:
                return search(start, middle_ind)
            return middle_ind

        return search(0, len(nums))
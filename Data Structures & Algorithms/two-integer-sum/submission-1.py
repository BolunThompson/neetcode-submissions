class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ndict = {v: i for i, v in enumerate(nums)}
        for i, v in enumerate(nums):
            if (target - v) in ndict and i != ndict[target - v]:
                return [i, ndict[target - v]]
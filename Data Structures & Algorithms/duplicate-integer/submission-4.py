class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nset = set()
        for n in nums:
            if n not in nset:
                nset.add(n)
            else:
                return True
        return False
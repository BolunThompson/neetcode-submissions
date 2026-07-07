# assuming sorted inductively:

def prefixes(nums):
    prod = 1
    for n in nums:
        yield prod
        prod *= n

def postfixes(nums):
    yield from reversed(list(prefixes(reversed(nums))))



class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ps = list(prefixes(nums))
        pf = list(postfixes(nums))

        result = [ps[i] * pf[i] for i in range(len(nums))]

        return result
    
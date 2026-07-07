# assuming sorted inductively:

def product(nums):
    r = 1
    for n in nums:
        r *= n
    return r

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero = False # index, False (none), True (2+)
        for i, n in enumerate(nums):
            if n != 0:
                prod *= n
            elif zero is False:
                zero = i
            # zero is true or a promotable int
            else:
                zero = True

        match zero:
            case True:
                return [0 for _ in nums]
            case False:
                return [prod // v for v in nums]
            case int(index):
                return [0 if i != zero else prod for i in range(len(nums))]

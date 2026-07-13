class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # n log n
        res = set()
        for i, v in enumerate(nums):
            # search for the matching pair
            j = 0
            k = len(nums) - 1
            while j < k:
                if i == j:
                    j += 1
                elif i == k:
                    k -= 1
                else:
                    residual = v + nums[j] + nums[k]
                    if residual == 0:
                        res.add(tuple(sorted([v, nums[j], nums[k]])))
                        j += 1
                        k -= 1
                    elif residual < 0:
                        j += 1
                    else:
                        k -= 1
        return list(map(list, res))
        # TODO: Finish, then AI. After done with this
        # launch issues and write!
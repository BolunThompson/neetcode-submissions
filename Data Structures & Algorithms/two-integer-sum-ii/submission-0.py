class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        find = 0
        bind = len(numbers) - 1
        while find < bind and find >= 0 and bind < len(numbers):
            first = numbers[find]
            last = numbers[bind]
            if (first + last) > target:
                bind -= 1
            elif (first + last) < target:
                find += 1
            else:
                return [find + 1, bind + 1]
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = Counter()
        for c in s:
            counter[c] += 1
        for c in t:
            counter[c] -= 1
            if counter[c] < 0:
                return False
        return all(n == 0 for n in counter.values())

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1counts = Counter(s1) # constnat, since s1 is only lower case
        si = 0
        for ei, v in enumerate(s2):
            assert s1counts[v] >= 0
            s1counts[v] -= 1
            # shift sliding window if counts is invalid
            while s1counts[v] < 0:
                s1counts[s2[si]] += 1
                si += 1
            if ei - si + 1 == len(s1):
                return True
        
        return False
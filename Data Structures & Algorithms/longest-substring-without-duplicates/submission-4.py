class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # TODO: Fix.
        seen = {} # character to ind
        best = 0
        cnt = 0
        window_start = 0
        for i, ch in enumerate(s):
            # TODO: Fix?
            # and is part of window
            if (repeat := seen.get(ch, -1)) >= window_start:
                # exclusive, exclusive
                cnt = i - repeat - 1
                window_start = repeat + 1
            cnt += 1
            best = max(best, cnt)
            seen[ch] = i
            print(i, repeat, cnt, best)
        
        return best
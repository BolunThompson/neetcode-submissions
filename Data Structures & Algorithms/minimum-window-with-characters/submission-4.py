class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # if not present in t and at back shrink.
        # if too many -> shrink.
        cnts = Counter(t)
        def is_stubble(c):
            return cnts.get(c, -1) < 0

        si = 0
        stubble = 0
        found = False
        best_si, best_ei = 0, len(s) - 1
        for ei, v in enumerate(s):
            if v in cnts:
                cnts[v] -= 1
            if is_stubble(v):
                stubble += 1
            while is_stubble(s[si]) and si < ei:
                if s[si] in cnts:
                    cnts[s[si]] += 1
                stubble -= 1
                si += 1
            window_size = ei - si + 1
            cover = window_size - stubble
            # cover - extra must be length of t, so it's t
            if cover == len(t) and window_size <= (best_ei - best_si + 1):
                print("found", si, ei)
                best_si, best_ei = si, ei
                found = True

        
        return s[best_si: best_ei + 1] if found else ""

                
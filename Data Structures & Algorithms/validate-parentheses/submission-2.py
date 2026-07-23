class Solution:
    def isValid(self, s: str) -> bool:
        parens = []
        PAIRS = {p[0]: p[1] for p in ("()", "{}", "[]")}

        for v in s:
            if v in PAIRS:
                parens.append(v)
            elif not parens or PAIRS[parens[-1]] != v:
                return False
            else:
                parens.pop()
        
        return not bool(parens)
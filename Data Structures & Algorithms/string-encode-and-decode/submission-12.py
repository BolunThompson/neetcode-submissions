def encode_str(s: str):
    return f"{len(s)} {s}"

def find_delim(s):
    for i, v in enumerate(s):
        if v == " ":
            return i

def decode_str(s):
    delim = find_delim(s)
    length = int(s[:delim])
    start = delim + 1
    end = delim + 1 + length
    return s[start:end], s[end:]

def decode_str_rec(s):
    if not s:
        return []
    first, suffix = decode_str(s)
    return [first] + decode_str_rec(suffix)

class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join(encode_str(s) for s in strs)

    def decode(self, s: str) -> List[str]:
        return decode_str_rec(s)
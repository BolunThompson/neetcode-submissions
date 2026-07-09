

class Solution:
    def isPalindrome(self, s: str) -> bool:
        fiter = (c.lower() for c in s if c.isalnum())
        biter = (c.lower() for c in reversed(s) if c.isalnum())
        return all(f == b for f, b in zip(fiter, biter))
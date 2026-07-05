from collections import *

def hashDict(d):
    return hash(frozenset(d.items()))

def angram_hash(s):
    return hashDict(Counter(s))

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        v = defaultdict(list)
        for s in strs:
            v[angram_hash(s)].append(s)
        return list(v.values())
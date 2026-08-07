import bisect

class TimeMap:
    def __init__(self):
        self.store: defaultdict[str, tuple[int, str]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # sorted by timestamp 
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        items = self.store[key]
        ind = bisect.bisect(items, timestamp, key=lambda v: v[1])
        if ind == 0:
            return ""
        return items[ind - 1][0]

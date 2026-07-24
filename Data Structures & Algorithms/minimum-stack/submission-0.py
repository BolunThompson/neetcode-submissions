class MinStack:
    lst: list
    minimums: list[int]
    # TODO: Finish but this is trivial with a list.

    def __init__(self):
        self.lst = []
        self.minimums = []

    def push(self, val: int) -> None:
        self.lst.append(val)
        mini = min(val, self.minimums[-1]) if self.minimums else val
        self.minimums.append(mini)

    def pop(self) -> None:
        self.minimums.pop()
        return self.lst.pop()

    def top(self) -> int:
        return self.lst[-1]

    def getMin(self) -> int:
        return self.minimums[-1]        

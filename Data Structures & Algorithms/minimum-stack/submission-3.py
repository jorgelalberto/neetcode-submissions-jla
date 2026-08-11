class MinStack:

    def __init__(self):
        self.stop = -1
        self.empty = True
        self.stack = []
        self.minNums = []

    def push(self, val: int) -> None:
        minNum = val
        if not self.empty:
            minNum = min(self.minNums[self.stop], val)

        if len(self.stack) == self.stop+1:
            self.stack.append(val)
            self.minNums.append(minNum)
        else:
            self.stack[self.stop+1] = val
            self.minNums[self.stop+1] = minNum

        self.empty = False
        self.stop += 1

    def pop(self) -> None:
        self.stop -= 1
        if self.stop == -1:
            self.empty = True

    def top(self) -> int:
        return self.stack[self.stop]

    def getMin(self) -> int:
        return self.minNums[self.stop]

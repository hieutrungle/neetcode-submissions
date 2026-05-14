import heapq

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_vals = [float('inf')]

    def push(self, val: int) -> None:
        self.min_vals.append(min(self.min_vals[-1], val))
        self.stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        self.min_vals.pop()

    def top(self) -> int:
        val = self.stack[-1]
        return val

    def getMin(self) -> int:
        return self.min_vals[-1]

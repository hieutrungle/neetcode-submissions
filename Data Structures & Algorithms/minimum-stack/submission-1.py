import heapq

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_vals = []

    def push(self, val: int) -> None:
        if self.min_vals:
            cur_min = min(self.min_vals[-1], val)
        else:
            cur_min = val
        self.min_vals.append(cur_min)
        self.stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        self.min_vals.pop()

    def top(self) -> int:
        val = self.stack[-1]
        return val

    def getMin(self) -> int:
        return self.min_vals[-1]

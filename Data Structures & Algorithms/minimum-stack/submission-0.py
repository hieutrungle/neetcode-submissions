import heapq

class MinStack:

    def __init__(self):
        self.min_heap = []
        self.stack = []
        self.idxs = set([])
        self.idx = 0

    def push(self, val: int) -> None:
        self.stack.append((val, self.idx))
        heapq.heappush(self.min_heap, (val, self.idx))
        self.idxs.add(self.idx)
        self.idx += 1

    def pop(self) -> None:
        val, idx = self.stack.pop()
        self.idxs.remove(idx)
        while self.min_heap and self.min_heap[0][1] not in self.idxs:
            heapq.heappop(self.min_heap)

    def top(self) -> int:
        val, idx = self.stack[-1]
        return val

    def getMin(self) -> int:
        return self.min_heap[0][0]

import bisect

class TimeMap:

    def __init__(self):
        self.d = defaultdict(list) # key: (val, timestamp)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""

        array = self.d[key]
        r = bisect.bisect_right(array, timestamp, key=lambda x: x[0])
        if r == 0:
            return ""
        else:
            return array[r - 1][1]
        
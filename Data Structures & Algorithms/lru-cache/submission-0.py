class DoublyList:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = DoublyList(-1, -1)
        self.tail = DoublyList(-1, -1, self.head)
        self.head.next = self.tail
        self.history = {}

    def remove(self, node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

        node.prev = None
        node.next = None

    def add(self, node):
        prev = self.head
        next = self.head.next

        prev.next = node
        next.prev = node

        node.next = next
        node.prev = prev

    def get(self, key: int) -> int:
        if key not in self.history:
            return -1
        
        node = self.history[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.history:
            self.history[key].val = value
            self.get(key)
            return

        node = DoublyList(key, value)
        self.history[key] = node
        self.add(self.history[key])
        if len(self.history) > self.capacity:
            last_node = self.tail.prev
            self.remove(last_node)
            self.history.pop(last_node.key)
        return
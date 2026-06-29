"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        root = node
        new_node = Node(node.val)
        d = {node: new_node} # old node -> new node
        queue = deque([node])
        while queue:
            node = queue.popleft()
            new_neighbors = []
            for next_node in node.neighbors:
                if next_node not in d:
                    new_next_node = Node(next_node.val)
                    d[next_node] = new_next_node
                    queue.append(next_node)
                new_neighbors.append(d[next_node])
            d[node].neighbors = new_neighbors

        return d[root]


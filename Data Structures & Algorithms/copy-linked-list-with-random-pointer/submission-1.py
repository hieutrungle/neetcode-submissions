"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d = {None: None}
        
        dummy2 = Node(-1)
        node1 = head
        node2 = dummy2
        while node1:
            node = Node(node1.val)
            node2.next = node
            d[node1] = node
            node1 = node1.next
            node2 = node2.next
        
        node1 = head
        while node1:
            random_node = node1.random
            copy_node = d[node1]
            if random_node:
                copy_random_node = d[random_node]
            else:
                copy_random_node = None
            copy_node.random = copy_random_node
            node1 = node1.next

        return dummy2.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        node = head
        visited = set()
        cnt = 0
        while node:
            node.val = float('inf')
            node = node.next
            if node and node.val == float('inf'):
                return True
        return False
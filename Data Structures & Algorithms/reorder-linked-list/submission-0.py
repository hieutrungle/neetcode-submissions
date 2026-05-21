# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next:
            return
        
        # slow and fast
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse
        node = slow.next
        slow.next = None
        prev = None
        while node:
            next = node.next
            node.next = prev
            prev = node
            node = next

        node2 = prev
        node1 = head
        # merge
        while node2:
            next1 = node1.next
            next2 = node2.next
            node1.next = node2
            node2.next = next1
            node1 = next1
            node2 = next2

        return
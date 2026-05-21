# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        node = head
        node2 = dummy
        
        cnt = 0
        while node:
            if cnt >= n:
                node2 = node2.next
            node = node.next
            cnt += 1
        next2 = node2.next
        node2.next = next2.next if next2 is not None else None
        
        return dummy.next
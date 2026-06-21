# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        heap = []
        for idx, l in enumerate(lists):
            heapq.heappush(heap, (l.val, idx))
            # lists[idx] = lists[idx].next

        node = dummy
        while heap:
            val, idx = heapq.heappop(heap)
            node.next = lists[idx]
            lists[idx] = lists[idx].next
            node = node.next
            if lists[idx]:
                heapq.heappush(heap, (lists[idx].val, idx))

        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # start_node, end_node --> reverse --> continue
        # is start_node_idx - start_node_idx < k: do nothing
        if not head or not head.next or k == 1:
            return head

        dummy = ListNode(0, head)
        # group_prev points to the node immediately BEFORE the current k-group
        group_prev = dummy
        
        while True:
            # 1. Find the k-th node to ensure we have a full group to reverse
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    break
            
            # If we don't have k nodes left, leave them as is and break
            if not kth:
                break
                
            # 2. Keep track of the node right after the k-group
            group_next = kth.next
            
            # 3. Reverse the group
            prev = group_next      # Start prev at group_next to automatically connect the new tail
            curr = group_prev.next # curr is the first node in the k-group
            
            for _ in range(k):
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                
            # 4. Reconnect the reversed group back to the main list
            # group_prev.next is the original start of the group (which is now the tail)
            temp = group_prev.next 
            
            # Connect the end of the previous group to the new head of this reversed group
            group_prev.next = kth 
            
            # Move group_prev forward to the tail of the newly reversed group for the next iteration
            group_prev = temp
            
        return dummy.next
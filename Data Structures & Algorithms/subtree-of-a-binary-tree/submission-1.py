# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True

        stack_r = [root]
        while stack_r:
            node = stack_r.pop()
            if node.val == subRoot.val:
                if self.isSame(node, subRoot):
                    return True
            if node.left:
                stack_r.append(node.left)
            if node.right:
                stack_r.append(node.right)
        return False

    def isSame(self, q, p):
        if not q and not p:
            return True
        if q and p and q.val == p.val:
            return self.isSame(q.left, p.left) and self.isSame(q.right, p.right)
        else:
            return False
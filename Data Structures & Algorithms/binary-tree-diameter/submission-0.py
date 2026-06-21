# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        if not root:
            return 0

        def dfs(node):
            if not node:
                return 0

            max_left = dfs(node.left)
            max_right = dfs(node.right) 
            self.res = max(self.res, max_left + max_right)
            return max(max_left, max_right) + 1

        dfs(root)
        return self.res
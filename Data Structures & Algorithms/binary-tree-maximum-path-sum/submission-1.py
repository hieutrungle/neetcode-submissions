# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')
        if not root:
            return 0
        
        def dfs(node):
            
            if not node:
                return 0

            cur_val = node.val
            tmp = cur_val
            if node.left:
                left = dfs(node.left)
                cur_val += left
                tmp = max(tmp, node.val + left)
            if node.right:
                right = dfs(node.right)
                cur_val += right
                tmp = max(tmp, node.val + right)
            self.res = max(cur_val, self.res)
            return max(0, tmp)

        dfs(root)
        return self.res
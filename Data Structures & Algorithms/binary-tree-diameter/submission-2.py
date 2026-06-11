# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        path = 0
        def dfs(curr):
            depth = 0
            if not curr:
                return 0
            left = dfs(curr.left)
            right = dfs(curr.right)
            nonlocal path
            path = max(path, left + right)
            return max(left, right) + 1
        dfs(root)
        return path
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True
        def dfs(curr):
            nonlocal balanced
            if not curr:
                return 0
            l = dfs(curr.left)
            r = dfs(curr.right)
            if l - r > 1 or r - l > 1:
                balanced = False
            return max(l, r) + 1
        dfs(root)
        return balanced
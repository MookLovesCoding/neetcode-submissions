# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        curr_max = root.val
        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal curr_max
            if not root:
                return 0
            curr = root.val
            left = max(0, dfs(root.left))
            right = max(0, dfs(root.right))
            curr_max = max(curr_max, (curr + left + right))
            return max((curr + left), (curr + right), curr)
        dfs(root)
        return curr_max
        
            
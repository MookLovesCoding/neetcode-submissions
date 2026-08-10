# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        smallest = min(p.val, q.val)
        biggest = max(p.val, q.val)
        while curr.val < smallest or curr.val > biggest:
            if curr.val < smallest:
                curr = curr.right
            else:
                curr = curr.left
        return curr
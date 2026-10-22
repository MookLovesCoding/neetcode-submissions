# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        serialized = []
        def dfs(root):
            if not root:
                serialized.append('null')
                return
            serialized.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ",".join(serialized)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if len(data) == 0:
            return None
        list_form = data.split(",")
        self.i = 0
        def dfs2():
            if list_form[self.i] == "null":
                self.i += 1
                return None
            node = TreeNode(int(list_form[self.i]))
            self.i += 1
            node.left = dfs2()
            node.right = dfs2()
            return node
            
        return dfs2()


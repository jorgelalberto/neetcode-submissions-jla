# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertRoot(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        temp = root.left
        root.left = root.right
        root.right = temp
        return root

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.right = self.invertTree(root.right)
        root.left = self.invertTree(root.left)

        return self.invertRoot(root)
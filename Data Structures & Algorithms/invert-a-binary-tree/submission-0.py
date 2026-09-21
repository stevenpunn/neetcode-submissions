# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # basic DFS search
        if not root:        # base case
            return None
        
        # swap root's left and right pointers
        root.left, root.right = root.right, root.left

        # recursively call DFS on both left and right child
        self.invertTree(root.left)
        self.invertTree(root.right)

        # return current node (inverted)
        return root
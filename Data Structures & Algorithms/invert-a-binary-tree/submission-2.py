# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # use DFS
        # base case:
        if not root:
            return None

        # swap the left and right pointers
        root.left, root.right = root.right, root.left

        # recursively call dfs on the new left child
        self.invertTree(root.left) 
        # after this, this calls the swap on line 15
        # if its called on a node w/ no children, it returns the root
        # then it will call invert on the right root of the same parent

        # call dfs on the new right child
        self.invertTree(root.right)

        return root

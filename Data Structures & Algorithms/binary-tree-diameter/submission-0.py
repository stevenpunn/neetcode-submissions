# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            # allows res to be modified outside the scope
            nonlocal res
            if not root:
                return 0
            # recursively compute left height
            left = dfs(root.left)
            # recursively compute right height
            right = dfs(root.right)
            # if the longest path is through left+right, stop
            res = max(res, left + right)

            # return height of the current node
            return 1 + max(left, right)
        # this is the line that starts the recursion
        dfs(root)
        return res        
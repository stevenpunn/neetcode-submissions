# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # instead of recursively searching, we can simulate DFS using a stack 
        # stack stores current node, and depth of current node
        # every pop from the stack, update max depth seen, push left & right children onto stack w/ depth + 1
        
        # initialize stack with pair (root, 1) for depth 1
        stack = [[root, 1]]
        maxDepth = 0

        # while the stack isn't empty
        while stack:
            node, depth = stack.pop()

            if node:    # checks if there is a current node
                maxDepth = max(maxDepth, depth)
                # push left node and depth + 1 onto stack if left child exists
                stack.append([node.left, depth+1])
                # push right node and depth + 1 onto stack if right child exists
                stack.append([node.right, depth+1])
        return maxDepth

'''
- Line 25 and 27 are executed together, adding both nodes and depths into the stack
- Then line 20 is ran after to pop them from the stack retreiving their depths
- Then line 23 is ran to update the maxDepth
- null nodes are added, but depth not considered due to the if condition
'''
        

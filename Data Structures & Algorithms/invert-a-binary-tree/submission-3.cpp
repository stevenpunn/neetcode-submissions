/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        // iterative DFS
        /*
        so in this process, every node is pushed onto the stack and swap is called
        first, the root is added, then popped (the popped node is the one having things done on it)
        then its children get swapped and then the node is removed
        the if statement checks if there are children that need to be pushed to the stack
        */
        if (!root){
            return nullptr;
        }
        stack<TreeNode*> stack;
        stack.push(root);
        // while the stack isn't empty
        while(!stack.empty()){
            TreeNode* node = stack.top();   // takes the top node
            // pop a node
            stack.pop();
            // swap the left and right pointers
            swap(node->left, node->right);
            // if the left child exists, push it to the stack
            if (node->left){
                stack.push(node->left);
            }
            // if the right child exists, push it to the stack
            if (node->right){
                stack.push(node->right);
            }
        }
        return root;
    }
};

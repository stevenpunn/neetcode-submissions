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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        // using recursive DFS
        // if both trees dont exist, they are equal
        if (!p && !q){
            return true;
        }
        // only executes if both trees and subtree comparisons are identical
        if (p && q && p->val == q->val){
            // this compares the subtree of p and q 
            // if the if statement is true, it recurses to check the children and subtrees
            return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
        } else {
            return false;
        }
    }
};

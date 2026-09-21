/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        // need to use ListNode* because it stores the addrss of a node, not the value directly
        ListNode* prev = nullptr;   // becomes the new head when done
        ListNode* curr = head;      // start at the original head

        while(curr){
            // we need to use -> instead of . because it is a pointer to the objext
            ListNode* temp = curr->next;    // save where the curr's next node is before changing
            curr->next = prev;              // reverse the curr's pointer, points backwards
            prev = curr;                    // move prev to the curr
            curr = temp;                    // move curr to the node we saved at the first step
        }
        return prev;
    }
};

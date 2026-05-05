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
    // ListNode* head: head is a pointer to a node in a linked list
    // head->next: go to the node head is pointing to
    ListNode* reverseList(ListNode* head) {
        // base case, if the list is empty, return null
        if (!head){
            return nullptr;
        }

        // placeholder for the new final result
        ListNode* newHead = head;
        // if there is a next head to process
        if (head->next){
            // reverse the rest of the list after the current node
            // stores the end as the head of the new list
            newHead = reverseList(head->next);
            // this makes the next node point to the current node
            head->next->next = head;
        }
        // breaks the forward cycle
        head->next = nullptr;

        return newHead;
    }
};

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
    void reorderList(ListNode* head) {
        // we can use reverse and merge
        // first find the middle of the linked list using slow and fast pointers
        ListNode* slow = head;
        ListNode* fast = head->next;
        // when fast is the end, slow is the middle
        while(fast != nullptr && fast->next != nullptr){
            slow = slow->next;
            fast = fast->next->next;
        }

        // reverse the second half of the liked list
        ListNode* second = slow->next;
        ListNode* prev = slow->next = nullptr;
        while(second != nullptr){
            ListNode* temp = second->next;
            second->next = prev;
            prev = second;
            second = temp;
        }

        // now merge the two
        ListNode* first = head;
        second = prev;
        while (second != nullptr){
            ListNode* temp1 = first->next;
            ListNode* temp2 = second->next;
            first->next = second;
            second->next = temp1;
            first = temp1;
            second = temp2;
        }
    }
};

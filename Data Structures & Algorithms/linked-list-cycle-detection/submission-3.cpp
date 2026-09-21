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
    bool hasCycle(ListNode* head) {
        // we can use a fast and slow pointer, if they match then we have a loop
        ListNode* slow = head;
        ListNode* fast = head;
        // if fast reaches end (null or fast.next is null), no cycle exists so return false
        while(fast != nullptr && fast->next != nullptr){
            fast = fast->next->next;
            slow = slow->next;

            if(fast == slow){
                return true;
            }
        }
        return false;
    }
};

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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        // iteratively
        ListNode dummy(0);          // create dummy on the stack
        ListNode* node = &dummy;    // &dummy since it is a local stack variable, so automatically cleaned up

        // each iteration compare current front of both lists and attach smaller onto node->next
        // then advance past the node we just used
        while(list1 && list2){
            if (list1->val < list2->val){
                node->next = list1;
                list1 = list1->next;
            }
            else {
                node->next = list2;
                list2 = list2->next;
            }
            node = node->next;
        }
        // cleanup, if one list completes, attach the leftover to the remaining chain
        if(list1){
            node->next = list1;
        }
        else{
            node->next = list2;
        }
        // dummy is not the answer, but dummy.next is the actual head of the merged list
        return dummy.next;
    }
};

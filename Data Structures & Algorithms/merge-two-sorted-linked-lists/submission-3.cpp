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
        if(!list1){
            return list2;
        }
        if(!list2){
            return list1;
        }
        if(list1->val < list2->val){
            // if list1 current node is smaller, it belongs first
            // whatever after in the mergeed result is merging the rest of list1 with list2
            list1->next = mergeTwoLists(list1->next, list2);
            return list1;
        } else {
            list2->next = mergeTwoLists(list1, list2->next);
            return list2;
        }
    }
};
/*
merge([1,2], [3,4])
1 < 2 so merge->next = merge([2], [3,4]) now it waits, doesn't return yet
3 > 2, so list2->next = merge([3], [4]), return list2 (node holding 2)


*/
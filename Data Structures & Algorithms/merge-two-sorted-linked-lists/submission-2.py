# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # using recursion
        # pick the smaller head node, recursively merge the rest of the lists
        # mergeList(l1, l2) returns head of merged sorted list of all nodes from l1 and l2

        if list1 is None:
            return list2
        if list2 is None:
            return list1
        # compare the head values of l1 and l2
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)  # l1.next = merge_the_rest
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        
    # l1 = 1 -> 3 -> 5
    # l2 = 2 -> 4 -> 6
    # first call compares 1 <= 2
    # after, then it compares the rest of each list, so 1.next = (3, 5) <= (2, 4, 6)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # iterative approach
        # have a pointer at the beginning of a list, keep the smaller node and keep going
        dummy = node = ListNode()

        while list1 and list2:          # comparing the two head nodes
            if list1.val < list2.val:
                node.next = list1       # smaller node is node.next
                list1 = list1.next      # if this list is chosen, move forward
            else:
                node.next = list2
                list2 = list2.next      # smaller node is node.next
            node = node.next            # if this liust is chosen, move forward

        node.next = list1 or list2

        return dummy.next
        # T(n) = O(n + m)
        # S(n) = O(1)
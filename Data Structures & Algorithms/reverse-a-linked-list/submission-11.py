# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            temp = curr.next    # this saves the next node
            curr.next = prev    # swaps the pointers next to each other
            prev = curr         # moves the previous pointer to the current pointer
            curr = temp         # moves the current pointer to the saved next pointer
        return prev
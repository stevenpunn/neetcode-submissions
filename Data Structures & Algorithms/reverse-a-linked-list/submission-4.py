# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # given 1 -> 2 -> 3 -> 4, we want 1 <- 2 <- 3 <- 4, reversing the arrows
        # need to consider what info we need to keep and remember
        prev = None
        curr = head

        while curr:
            temp = curr.next    # this will store the next node
            curr.next = prev    # save the next node as the previous node, this swaps the arrow direction
            prev = curr         # move previous to current
            curr = temp         # move curr to temp (move 1 node up)
        return prev     # return prev (new head of the linked list)
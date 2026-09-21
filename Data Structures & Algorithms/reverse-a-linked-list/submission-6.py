# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # complete this recursively 
        if not head:        # base case
            return None

        newHead = head      #newHead initialized to the head
        if head.next:       # if there is a next node to process
            newHead = self.reverseList(head.next)   # newHead is stored, then the rest is reversed
            head.next.next = head
        head.next = None        # this sets the next (last) node to null

        return newHead
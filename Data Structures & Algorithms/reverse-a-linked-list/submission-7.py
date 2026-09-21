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
            temp = curr.next    # go to the next node
            curr.next = prev    # this is the key step that reverses the arrows
            prev = curr         # this moves the pointer to the right
            curr = temp         # this moves the pointer right 1 more time
        return prev
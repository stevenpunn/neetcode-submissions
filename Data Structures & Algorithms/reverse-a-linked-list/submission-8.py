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
            temp = curr.next    # save the next code
            curr.next = prev    # reverse the pointer
            prev = curr         # move prev to curr
            curr = temp         # move curr to temp
        return prev
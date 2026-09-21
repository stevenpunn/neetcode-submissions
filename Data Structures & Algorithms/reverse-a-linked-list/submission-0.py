# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # use iterative approach
        # for each node, redirect its next pointer to point to the node behind it
        # curr = current node 
        # prev = node after curr once reversed
        # temp = original next node
        prev = None
        curr = head

        while curr:
            temp = curr.next    # savees the next node
            curr.next = prev    # reverse the pointer
            prev = curr
            curr = temp
        return prev             # prev becomes the new head of the reversed list
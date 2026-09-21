# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # O(n) time, O(1) space
        # iterative approach, swap pointers one step at a time
        # move through the list from left to right and for each node, 
        # redicted the next pointer to point to a node behind it
        # don't think of this as swapping the nodes, but swapping the arrows pointing to the next node
        prev = None
        curr = head

        while curr:             # while the current node exists
            temp = curr.next    # save the next node as temp    
            curr.next = prev    # reverse the pointer
            prev = curr         # move the previous pointer to current 
            curr = temp
        return prev
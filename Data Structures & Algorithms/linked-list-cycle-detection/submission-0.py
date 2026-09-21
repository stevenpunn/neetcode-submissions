# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # create a hashset to store visited nodes
        seen = set()
        # start with the head node
        curr = head
        while curr:
            if curr in seen:
                return True
            # if not seen, add to hash set
            seen.add(curr)
            curr = curr.next
        return False
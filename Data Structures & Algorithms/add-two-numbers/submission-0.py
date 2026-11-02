# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # using iteration
        # first use a dummy node to build the answer
        # curr node points to dummy
        # integer carry to represent carry over addition
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            # read the current digit of each list (0 if already ended)
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # creating new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            # append a new node containing digit
            cur.next = ListNode(val)

            # update the pointers, moving them forward
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

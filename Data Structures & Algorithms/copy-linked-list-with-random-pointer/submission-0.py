"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # use a hash map to copy a linked list where every node has a next pointer and a random pointer
        # hash map can create nodes and point nodes in 2 passes simultaneously

        # we can create a hashmap that returns an empty node when we access a key that doesn't exist
        oldToCopy = collections.defaultdict(lambda: Node(0))
        # oldToCopy[null] = null so next or random can safely point to null
        oldToCopy[None] = None

        # traverse the list only once
        cur = head
        while cur:
            # set the copied node's value
            oldToCopy[cur].val = cur.val
            # link the current node's next pointer using the map
            oldToCopy[cur].next = oldToCopy[cur.next]
            # link the random pointer using the map
            oldToCopy[cur].random = oldToCopy[cur.random]
            # move the current pointer
            cur = cur.next
        return oldToCopy[head]
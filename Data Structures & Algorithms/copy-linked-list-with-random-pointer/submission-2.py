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
        old_to_new = {None: None}

        # creates and copies (but user only concerned w/ get)
        def get_copy(node: 'Optional[Node]'):
            if node == None:
                return None

            if node not in old_to_new:
                old_to_new[node] = Node(node.val, None, None)

            return old_to_new[node]

        headStart = head
        headCopy = head

        while head:
            headCopy = get_copy(head)
            headCopy.next = get_copy(head.next)
            headCopy.random = get_copy(head.random)
            head = head.next
        return get_copy(headStart)
